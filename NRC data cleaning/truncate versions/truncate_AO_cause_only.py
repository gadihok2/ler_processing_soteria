# coding: utf8
import json
import os
import sys
import re
import fileinput
from HTMLParser import HTMLParser
import re
import simplejson
from pytictoc import TicToc

"""
Borrowed from https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
"""
class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)
"""
Borrowed from https://stackoverflow.com/questions/753052/strip-html-from-strings-in-python

"""
def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
    print ()


"""
Split the given text into paragraphs based on the given delimeter. Returns a list of strings (paragraphs) with the
HTML stripped.
"""
def split_text_into_pars(text, delimiter):
    pars = text.split(delimiter)
    for i in range(len(pars)):
        pars[i] = strip_tags(pars[i])
    return pars


"""
Creates a new formatted entry in the output file
"""
def new_output_entry(output_file, ml, cat, par_num, text, z):
    new_entry = ml + "|" + str(z) + "|" + cat + "|" + str(par_num) + "|" + text + "\n"
    with open(output_file, "a") as f:
        f.write(new_entry)


"""
Separates the portion of text within the start/stop points from the text that is outside the start/stop points.
"""
def separate(begin, end, start, stop, text):
    inside_tags = text[begin + len(start):end]
    #outside_tags = text[:begin] + text[end + len(stop):]
    outside_tags = text
    return inside_tags, outside_tags


"""
Takes the action associated with the given anchors
"""
def process(contents, anchors, textfile):
    # Use the first start anchor that can be found in the html
    for start in anchors["start"]:
        if start == "DOC_START":
            begin = 0
        else:
            begin = contents.find(str(start))

        if begin != -1:
            break
    if begin == -1:
        #print("Unable to find any of the following start anchors: " + str(anchors["start"]) + ", a start anchor")

        return None, None, contents
    # Use the first stop anchor that can be found in the html
    for stop in anchors["stop"]:
        if stop == "DOC_END":
            end = len(contents)
        else:
            end = contents[begin + len(start):].find(str(stop))

        if end != -1:
                if stop != "DOC_END":
                    end += begin + len(start)
                break
    if end == -1:
        #print("Unable to find any of the following stop anchors: " + str(anchors["stop"]) +  ", a stop anchor")
        return None, None, contents
    inside, outside = separate(begin, end, start, stop, contents)
    return anchors["action"], inside, outside

# Function to make lists containing anchor pairs according to category

def list_maker(anchors):
    list_1 = []
    list_2 = []
    list_3 = []
    list_4 = []
    list_5 = []
    list_same_category = [list_1,list_2,list_3,list_4,list_5]
    for anchor_finder in anchors:
        if anchor_finder["category"] == "FACILITY NAME":
            list_1.append(anchor_finder)
        elif anchor_finder["category"] == "TITLE":
            list_2.append(anchor_finder)
        elif anchor_finder["category"] == "ABSTRACT":
            list_3.append(anchor_finder)
        elif anchor_finder["category"] == "DESCRIPTION":
            list_4.append(anchor_finder)
        elif anchor_finder["category"] == "CAUSE":
            list_5.append(anchor_finder)
    return list_same_category

# Function to calculate success rate (quantity metrics)

def success_rate(category,dict):
    if category == "FACILITY NAME":
        dict["facility"] += 1
    elif category == "TITLE":
        dict["title"] += 1
    elif category == "ABSTRACT":
        dict["abstract"] += 1
    elif category == "DESCRIPTION":
        dict["description"] += 1
    elif category == "CAUSE":
        dict["cause"] += 1
    return dict

# Function to calculate percentage

def percentage(part, whole):
  return round(100 * float(part)/float(whole) , 2)

# Function to calculate success rate (Quality Metric)
def how_is_the_output(cat, data):
    if cat == "ABSTRACT":
        if len(data)<=100:
            return True
    elif cat == "DESCRIPTION":
        if len(data)<=300:
            return True
    elif cat == "CAUSE":
        if "CORRECTIVE ACTIONS" in data:
            return True
        elif "Corrective Actions" in data:
            return True
    else:
        return False

def how_complete_is_the_output(cat, data):
    if cat == "ABSTRACT":
        if data[-1] != ".":
            return True
    elif cat == "DESCRIPTION":
        if data[-1] != ".":
            return True
    elif cat == "CAUSE":
        if data[-1] != ".":
            return True
    else:
        return False

# Function to replace text in place i.e. without changing the file

def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

# Function to refine final output (delete unnecessary text etc.)

def refine_ouput(file,patterns):
    list = ["to 1400 spaces, i.e., approximately 15 typewritten","to 1400 spaces, i.e., approximately 15 type written","to 1400 spaces, i.e., approximately 15 type written","to 1400 spaces, i.e., approximately 15 typewritten","to 1400 spaces, i.e., approximately 15 typewritten Ines","to 1400 spaces, i.e., approximately 15 typewritten ines","to 1400 spaces. i.e., approximately 15 typewritten","to 1400 spaces, i.e., approximately 15 typewritten","to 1400 spaces, Le., approximately 15 typewritten","to 1400 spaces, i.e., approximately 15 typewritten fines","to 1400 spaces, i.e approximately 15 typewritten","to 1400 spaces, i.e., approximately 15 single spaced typewritten","to 1400 spaces. i.e.. approximately 15 typewritten", "Corrective Action", "corrective action", "Corrective action", "Corrective Actions", "corrective actions", "Corrective actions", "Corrective", "corrective","SUBMISSION","EPIX","FORM","COMPONENT","DAY","YEAR","MONTH","DOCKET","REPORTABLE","REPORT","SUPPLEMENTAL","FACTURER","MANU","COMPONENT","SYSTEM"," CAUSE ","INOPERABLE ","STRUCTURES","SYSTEMS ","THAT ","CONTRIBUTED"," TO ","THE ","EVENT ","DATES ","AND ","APPROXIMATE ","TIMES ","OF ","MAJOR" ,"OCCURENCES","NUCLEAR ","REGULATORY ","COMMISSION ","LICENSEE", "EVENT", " LER ","PAGE ","SEQUENTIAL"," REVISION ","NUMBER","EXPECTED","NO ABSTRACT (16)","NO ABSTRACT","DATE 15","DATE","Limit","(14)"]
    replaceAll(file,'U- F', 'UF')
    replaceAll(file,'u- F', 'UF')
    replaceAll(file,'U-F', 'UF')
    replaceAll(file,'u-F', 'UF')
    replaceAll(file,'U-', 'U')
    replaceAll(file,'u-', 'u')
    replaceAll(file,'Feedwater', 'Feed water')
    replaceAll(file,'feedwater', 'feed water')
    replaceAll(file,'Overtemperature', 'Over temperature')
    replaceAll(file,'overtemperature', 'over temperature')
    replaceAll(file,'Undervoltage', 'Under voltage')
    replaceAll(file,'undervoltage', 'under voltage')
    replaceAll(file, 'U- ', 'UFACTURER ')
    for i in list:
        replaceAll(file,i,"")

    for j in patterns:
        replaceAll(file,j,"")
    return




# Function to remove whitespace from end of extracted text

def remove_space_from_end(extracted):
    if extracted[-1] == ' ':
        extracted = extracted[:-1]
    return extracted

def refiner(string):
    list_1 = string.split()
    list_2 = []
    list_3 = []
    #print list_1[1].isupper()
    #print list_1
    for i in list_1:
        #if "(" or ")" not in i:
        if i.isupper() == True:
            list_3.append(i)
        elif i.isdigit() == False and i.isalpha() == False:
            if i[-1] == ',' or i[-1] == '.':
                if i[0].isalpha() == True:
                    list_2.append(i)
                else:
                    list_3.append(i)
        else:
            list_2.append(i)
        #else:
        #   continue
    #print list_3
    output = " ".join(list_2)
    return output

def no_corrective_actions(data):
    if 'Corrective Actions' in data:
        index = data.find('Corrective Actions')
    elif 'CORRECTIVE' in data:
        index = data.find('CORRECTIVE')
    elif 'Corrective actions' in data:
        index = data.find('Corrective actions')
    elif 'corrective actions' in data:
        index = data.find('corrective actions')
    elif 'Corrective Action' in data:
        index = data.find('Corrective Action')
    elif 'Corrective action' in data:
        index = data.find('Corrective action')
    elif 'corrective action' in data:
        index = data.find('corrective action')
    else:
        return data

    data = data[:index]
    return data

def remover(string):
    string1 = 'to 1400'
    string2 = 'To 1400'
    i = string.find(string1)
    if i == -1:
        return string
    else:
        n = i + 71
        string = string.replace(string[i:n]," ")
        return string

def anchor_optimizer_checker(string):
    if string.count('(')>20 or string.count(')')>20 or string.count('5')>19 or string.count('•') >5:
        return True
    else:
        return False


def pp_1(string):
    list1 = ['single-spaced','SINGLE-SPACED','Single-spaced','single-space']
    for i in list1:
        if i in string:
            index = string.find(i)
            string = string[0:index-44] + string[index+30:]
            #print(string[index:index+30])
            #print(string)
        else:
            continue
    return string 

def reg_ex(extracted,list):
    search = re.search( r'.* (.*?) N/A', extracted)
    if search==None:
        return
    list.append(search.group())
    return list


def main(anchor_file, truncate_dir, output_file):
    open( output_file , 'w').close()
    with open(anchor_file) as f:
        anchors = simplejson.load(f)

        # Create initial counter lists (success metrics) and anchor lists

        list_same_category = list_maker(anchors)
        counting_dict = {"facility":0,"title":0,"abstract":0,"description":0,"cause":0}
        counting_missing = {"facility":0,"title":0,"abstract":0,"description":0,"cause":0}
        counting_missing_new_2 = {"facility":1,"title":1,"abstract":1,"description":1,"cause":1}
        missing_lers = {"FACILITY NAME":[],"TITLE":[],"ABSTRACT":[],"DESCRIPTION":[],"CAUSE":[]}
        incorrect_info_LER_1 = {"ABSTRACT":[],"DESCRIPTION":[],"CAUSE":[]}
        incorrect_info_LER_2 = {"ABSTRACT":[],"DESCRIPTION":[],"CAUSE":[]}
        incorrect_info_counter_1 = {"ABSTRACT":0,"DESCRIPTION":0,"CAUSE":0}
        incorrect_info_counter_2 = {"ABSTRACT":0,"DESCRIPTION":0,"CAUSE":0}
        success_counter = 0
        fail_counter = 0
        total_counter = 0
        partial_success = 0
        ending_chars_desc = []
        ending_chars_cause = []
        ending_chars_abstract = []
        patterns = []

        filenames = []
        t = TicToc()  # create instance of class
        times = []#start timer
        for filename in os.listdir(truncate_dir):
            start_time= t.tic()
        #skip over non LER files file and display the correct error message and file output
            # UNCOMMENT LINE BELOW TO INCLUDE YEARS BEFORE 2000
            #if filename.startswith('ML', 0, 2) or filename.startswith('98', 0, 2) or filename.startswith('99', 0, 2):
            if filename.startswith('i', 0, 2) == False and filename.startswith('o',0,2) == False :#and filename.startswith('2007',3,7):
                if filename in filenames:
                    continue
                else:
                    filenames.append(filename)
                    total_counter +=1
                    counting_missing_new = {"facility":0,"title":0,"abstract":0,"description":0,"cause":0}
                    remaining = ""
                    with open(os.path.join(truncate_dir, filename)) as f:
                        remaining = f.read().replace("\n", " ")
                        if "<br />" in remaining:
                            remaining = remaining.replace("<br />","<br>")
                    #list = []

                    ml = filename.split(".")[0]

                    
                    extracted = ''


                    for dict in anchors:


                        action, extracted_1, remaining = process(remaining, dict, filename)

                        if extracted_1 is None:
                            continue

                        
                        # Choose longest and cleanest extracted text
                        if anchor_optimizer_checker(extracted_1) == False and len(strip_tags(extracted_1))>len(strip_tags(extracted)):
                            extracted = extracted_1
                        else:
                            continue
                        
                
                    if anchor_optimizer_checker(extracted) == True:
                        print 'True'

                    cat = str(dict["category"])
                    if extracted == '' or extracted == '  ' or extracted == ' ' or extracted == '   ' :
                        extracted = 'COULD NOT FIND TEXT'
                        counting_dict = success_rate(cat,counting_dict)
                        counting_missing_new = success_rate(cat,counting_missing_new)
                        missing_lers[cat].append(ml)
                    else:
                        if cat == 'DESCRIPTION':
                            extracted = remove_space_from_end(extracted)
                            ending_chars_desc.append(extracted[-1])
                        elif cat == 'CAUSE':
                            extracted = remove_space_from_end(extracted)
                            ending_chars_cause.append(extracted[-1])
                        elif cat == 'ABSTRACT':
                            extracted = remove_space_from_end(extracted)
                            ending_chars_abstract.append(extracted[-1])

                        result_info_1 = how_is_the_output(cat,extracted)
                        result_info_2 = how_complete_is_the_output(cat,extracted)

                        if result_info_1 == True:
                            incorrect_info_counter_1[cat] += 1
                            incorrect_info_LER_1[cat].append(ml)

                        if result_info_2 == True:
                            incorrect_info_counter_2[cat] += 1
                            incorrect_info_LER_2[cat].append(ml)

                    extracted = " ".join(extracted.split())

                    #if cat == 'DESCRIPTION' or cat == 'ABSTRACT' or cat == 'CAUSE':
                        #extracted = refiner(extracted)

                    extracted = no_corrective_actions(extracted)
                    extracted = remover(extracted)

                    extracted = pp_1(extracted)
                    #patterns = reg_ex(extracted,patterns)

                    '''
                    #Need more work to confirm relevance of this

                    start_a = "Limit to 1400 "
                    stop_a = "lines"
                    if start_a in extracted:
                        begin_a = extracted.find(str(start_a))
                        end_a = extracted[begin_a:].find(str(stop_a))
                        inside_tags = extracted[begin_a : end_a + len(stop_a)+1]
                        extracted = extracted.replace(inside_tags, "")
                    '''

                    if cat != 'CAUSE' :
                        continue 
                    new_output_entry(output_file, ml, cat, 1, strip_tags(extracted), 1)

                    if counting_missing_new == counting_missing:
                        success_counter += 1
                    elif counting_missing_new == counting_missing_new_2:
                        fail_counter += 1
                    else:
                        partial_success += 1

                    '''
                    end_time = t.toc()
                    times.append(end_time)
                    try:
                        average = sum(times)/len(times)
                    except:
                        continue
                    #print average 
                    '''
                    # print statements for terminal output
                    
                    print "---------- NEW ENTRY -------------"
                    print "---------------GENERAL INFORMATION"
                    print str(total_counter) + " files in total"

                    print str(fail_counter) +  " complete extraction failure (" +  str(percentage(fail_counter,total_counter)) + "%)"
                    print str(success_counter) + " complete extraction success (" +  str(percentage(success_counter,total_counter)) + "%)"
                    print str(partial_success) + " partial extraction success (" +  str(percentage(partial_success,total_counter)) + "%)"
                    print "--------------SPECIFIC INFORMATION"
                    print str(counting_dict["facility"]) +  " Facility Names not found. (success rate =" +  str(100-percentage(int(counting_dict["facility"]),total_counter)) + "%)"
                    #print missing_lers["FACILITY NAME"]
                    print str(counting_dict["title"]) +  " Titles not found. (success rate =" +  str(100-percentage(int(counting_dict["title"]),total_counter)) + "%)"
                    #print missing_lers["TITLE"]
                    print str(counting_dict["abstract"]) +  " Abstracts not found. (success rate =" +  str(100-percentage(int(counting_dict["abstract"]),total_counter)) + "%)"
                    #print missing_lers["ABSTRACT"]
                    print str(counting_dict["description"]) +  " Descriptions not found. (success rate =" +  str(100-percentage(int(counting_dict["description"]),total_counter)) + "%)"
                    #print missing_lers["DESCRIPTION"]
                    print str(counting_dict["cause"]) +  " Causes not found. (success rate =" +  str(100-percentage(int(counting_dict["cause"]),total_counter)) + "%)"
                    #print missing_lers["CAUSE"]
                    print "--------------QUALITY METRICS"
                    print "NEW QUALITY METRICS NEEDED"
                    
                    '''
                    try:
                        print str(incorrect_info_counter_1["ABSTRACT"]) +  " Abstracts were too short. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["ABSTRACT"]),(total_counter-int(counting_dict["abstract"])))) + "%)"
                    except:
                        print str(incorrect_info_counter_1["ABSTRACT"]) +  " Abstracts were too short. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["ABSTRACT"]),total_counter)) + "%)"

                    #print incorrect_info_LER["ABSTRACT"]

                    try:
                        print str(incorrect_info_counter_1["DESCRIPTION"]) +  " Descriptions were shorter than expected. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["DESCRIPTION"]),(total_counter-int(counting_dict["description"])))) + "%)"
                    except:

                        print str(incorrect_info_counter_1["DESCRIPTION"]) +  " Descriptions were shorter than expected. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["DESCRIPTION"]),total_counter)) + "%)"

                    try:
                        print str(incorrect_info_counter_1["CAUSE"]) +  " Causes had the Corrective Actions in them. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["CAUSE"]),(total_counter-int(counting_dict["cause"])))) + "%)"
                    except:

                        print str(incorrect_info_counter_1["CAUSE"]) +  " Causes had the Corrective Actions in them. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["CAUSE"]),total_counter)) + "%)"


                    try:
                        print str(incorrect_info_counter_2["ABSTRACT"]) +  " Abstracts end with half a sentence indicating partial truncation. (failure rate =" +  str(percentage(int(incorrect_info_counter_2["ABSTRACT"]),(total_counter-int(counting_dict["abstract"])))) + "%)"
                    except:
                        print str(incorrect_info_counter_2["ABSTRACT"]) +  " Abstracts end with half a sentence indicating partial truncation. (failure rate =" +  str(percentage(int(incorrect_info_counter_2["ABSTRACT"]),total_counter)) + "%)"

                    #print incorrect_info_LER["ABSTRACT"]

                    try:
                        print str(incorrect_info_counter_2["DESCRIPTION"]) +  " Descriptions end with half a sentence indicating partial truncation. (failure rate =" +  str(percentage(int(incorrect_info_counter_2["DESCRIPTION"]),(total_counter-int(counting_dict["description"])))) + "%)"
                    except:

                        print str(incorrect_info_counter_2["DESCRIPTION"]) +  " Descriptions end with half a sentence indicating partial truncation. (failure rate =" +  str(percentage(int(incorrect_info_counter_1["DESCRIPTION"]),total_counter)) + "%)"

                    try:
                        print str(incorrect_info_counter_2["CAUSE"]) +  " Causes end with half a sentence indicating partial truncation. (failure rate =" +  str(percentage(int(incorrect_info_counter_2["CAUSE"]),(total_counter-int(counting_dict["cause"])))) + "%)"
                    except:

                        print str(incorrect_info_counter_2["CAUSE"]) +  " Causes end with half a sentence indicating partial truncation. (failure rate =" +  str(percentage(int(incorrect_info_counter_2["CAUSE"]),total_counter)) + "%)"
                    '''
                    
                    #print incorrect_info_LER["DESCRIPTION"]

                    #print ending_chars_desc
                    #print ending_chars_cause

                    '''
                    for anchor_pair in anchors:

                        ml = filename.split(".")[0]

                        cat = anchor_pair["category"]

                        action, extracted, remaining = process(remaining, anchor_pair, filename)
                        # Do not need to make an output entry if the action fails or is a "REMOVE" action
                        if extracted is None or action == "REMOVE":
                            continue


                        if cat in list:
                            continue
                        else:
                            list.append(cat)


                        # Further split the text into paragraphs if indicated by the input file
                        if "paragraphs" in anchor_pair and anchor_pair["paragraphs"]:
                            pars = split_text_into_pars(extracted, ". <br />")
                            for i, par in enumerate(pars):
                                new_output_entry(output_file, ml, cat, i+1, par)
                        else:

                        new_output_entry(output_file, ml, cat, 1, strip_tags(extracted))

                        '''
            else:
                continue

    refine_ouput(output_file,patterns)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python truncate.py <anchor_file_path> <truncate_dir> <output_file_path>")
        exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])

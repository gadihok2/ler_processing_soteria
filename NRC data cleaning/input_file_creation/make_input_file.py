import os
import sys
import shutil
import json
import copy
from shutil import copyfile

def path_maker(path,file):
    new = path + '/' + file
    return new

def main(master_folder):

    path_output = path_maker(master_folder,'inputs_combined.json')

    if os.path.isfile(path_output) == False:
        open(path_output,'w+')
    else:
        open( path_output , 'w').close()

    list = []

    for i in range(0,5):
        for file in os.listdir(master_folder):
            if file.startswith('.'):
                continue
            file_path = path_maker(master_folder,file)
            if file_path == path_output:
                continue
            else:
                data_open = open(file_path)
                data = json.load(data_open)
                dict = data[i]
                if dict in list:
                    continue
                else:
                    list.append(data[i])
                    '''
    list_2 = copy.deepcopy(list)

    for p in list_2:
        br = '<br>'
        br_new = '<br />'
        start_anch = str(p["start"])
        stop_anch = str(p["stop"])

        if br in start_anch:
            start_anch = start_anch.replace(br,br_new)
            p["start"] = start_anch

        if br in stop_anch:
            stop_anch = stop_anch.replace(br,br_new)
            p["stop"] = stop_anch

    list_final = list + list_2
    '''
    with open(path_output, 'w') as outfile:
        json.dump(list, outfile)
        outfile.close
        #break
if __name__ == '__main__':
	main(sys.argv[1])

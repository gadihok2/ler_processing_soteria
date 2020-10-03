import os
import sys
import shutil
from shutil import copyfile
import json
import requests

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

INPUT_FILE_PATH = ""
DOWNLOAD_DIR_PATH = ""
CHROME_DRIVER_PATH = ""

def _select_from_options(el, search_key, search_params):
    if search_key not in search_params:
        return
    search_value = search_params[search_key]
    for option in el.find_elements_by_tag_name('option'):
        if option.text.strip() == search_value:
            option.click()
            return


"""
Selects a checkbox element
"""
def _select_checkbox(el, search_key, search_params):
    if search_key in search_params and search_params[search_key] == "Select":
        el.click()


"""
Fill a textbox element
"""
def _fill_text(el, search_key, search_params):
    if search_key in search_params:
        el.send_keys(search_params[search_key])


"""
Executes a search query using the given search parameters.
@return True on success, False on failure
"""
def search(browser, search_params):
    browser.get("https://lersearch.inl.gov/LERSearchCriteria.aspx")

    # Find elements for search parameters
    event_start_month = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownEventStartMonth")
    event_start_day = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownEventStartDay")
    event_start_year = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownEventStartYear")

    event_end_month = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownEventEndMonth")
    event_end_day = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownEventEndDay")
    event_end_year = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownEventEndYear")

    report_start_month = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownReportStartMonth")
    report_start_day = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownReportStartDay")
    report_start_year = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownReportStartYear")

    report_end_month = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownReportEndMonth")
    report_end_day = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownReportEndDay")
    report_end_year = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownReportEndYear")

    reactor_type_bwr = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxReactorTypeBWR")
    reactor_type_pwr = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxReactorTypePWR")
    reactor_type_hgtr = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxReactorTypeHGTR")

    vendor_bw = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxBW")
    vendor_ce = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxCE")
    vendor_ge = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxGE")
    vendor_wh = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxWE")
    vendor_other = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxOther")

    plant = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_ListBoxPlantList")

    docket = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_ListBoxDocketList")

    nrc_region_i = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListNRCRegion_0")
    nrc_region_ii = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListNRCRegion_1")
    nrc_region_iii = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListNRCRegion_2")
    nrc_region_iv = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListNRCRegion_3")

    op_mode_pow_op = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_0")
    op_mode_startup = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_1")
    op_mode_pow_hot_standby = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_2")
    op_mode_hot_shut = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_3")
    op_mode_cold_shut = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_4")
    op_mode_refuel = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_5")
    op_mode_pow_other = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_CheckBoxListOperatingMode_6")

    reportability = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_ListBoxReportability")

    power_level_low = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownPowerLow")
    power_level_high = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_DropDownPowerHigh")

    keywords = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_TextBoxKeywords")

    display_all_in_one_page = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_ListBoxResultPerPage")


    # Enter search parameters from input file
    _select_from_options(event_start_month, "Event Start Month", search_params)
    _select_from_options(event_start_day, "Event Start Day", search_params)
    _select_from_options(event_start_year, "Event Start Year", search_params)
    _select_from_options(event_end_month, "Event End Month", search_params)
    _select_from_options(event_end_day, "Event End Day", search_params)
    _select_from_options(event_end_year, "Event End Year", search_params)
    _select_from_options(report_start_month, "Report Start Month", search_params)
    _select_from_options(report_start_day, "Report Start Day", search_params)
    _select_from_options(report_start_year, "Report Start Year", search_params)
    _select_from_options(report_end_month, "Report End Month", search_params)
    _select_from_options(report_end_day, "Report End Day", search_params)
    _select_from_options(report_end_year, "Report End Year", search_params)
    _select_checkbox(reactor_type_bwr, "Reactor Type BWR", search_params)
    _select_checkbox(reactor_type_pwr, "Reactor Type PWR", search_params)
    _select_checkbox(reactor_type_hgtr, "Reactor Type HGTR", search_params)
    _select_checkbox(vendor_bw, "Babcock & Wilcox", search_params)
    _select_checkbox(vendor_ce, "Combustion Engineering", search_params)
    _select_checkbox(vendor_ge, "General Electric", search_params)
    _select_checkbox(vendor_wh, "Westinghouse", search_params)
    _select_checkbox(vendor_other, "Vendor Other", search_params)
    _select_from_options(plant, "Plant", search_params)
    _select_from_options(docket, "Docket", search_params)
    _select_checkbox(nrc_region_i, "NRC Region I", search_params)
    _select_checkbox(nrc_region_ii, "NRC Region II", search_params)
    _select_checkbox(nrc_region_iii, "NRC Region III", search_params)
    _select_checkbox(nrc_region_iv, "NRC Region IV", search_params)
    _select_checkbox(op_mode_pow_op, "Power Operation", search_params)
    _select_checkbox(op_mode_startup, "Startup", search_params)
    _select_checkbox(op_mode_pow_hot_standby, "Hot Standby", search_params)
    _select_checkbox(op_mode_hot_shut, "Hot Shutdown", search_params)
    _select_checkbox(op_mode_cold_shut, "Cold Shutdown", search_params)
    _select_checkbox(op_mode_refuel, "Refuel", search_params)
    _select_checkbox(op_mode_pow_other, "Operating Mode Other", search_params)
    _select_from_options(reportability, "Reportability", search_params)
    _select_from_options(power_level_low, "Power Level Low", search_params)
    _select_from_options(power_level_high, "Power Level High", search_params)
    _select_from_options(display_all_in_one_page, "Results per Page", search_params)
    _fill_text(keywords, "Keywords", search_params)

    # Execute search
    browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_Button_SearchBottom").click()

    # Wait up to timeout*2 seconds for search results to show up
    timeout = 100
    try:
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.ID, "ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_TotalRecsLabel")))
        num_results = browser.find_element_by_id('ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_TotalRecsLabel')
        # Search is considered a failure if there are no downloadable file results
        if num_results.text == "0":
            return False
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//table[@id='ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults']/tbody")))
    except TimeoutException:
        print("Timed out waiting for search results page to load")
        return False
    return True

def name_changer(browser):
    results_table = browser.find_element_by_id("ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults")
    dload_count = 0
    dload_count_skipped = 0
    gen_counter = 0
    file_list = []
    for file_1 in os.listdir(DOWNLOAD_DIR_PATH):
    	file_list.append(file_1.split(".")[0])

    while (True):
        for row in browser.find_elements_by_xpath("//tr[.//span[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults_LabelAccessionNum_')]]"):
            gen_counter+=1
            print gen_counter
            #link_0 = row.find_elements_by_xpath(".//span[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults_LabelLERNum_')]/a")
            
            accession = row.find_elements_by_xpath(".//span[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults_LabelAccessionNum_')]")[0].text
            	
            if accession in file_list:
                #link = row.find_elements_by_xpath(".//span[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults_LabelLERNum_')]/a")[1]
                try:
                	ler_number = row.find_elements_by_xpath(".//span[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults_LabelLERNum_')]/a")[0].text
                except:
                	#ler_number = row.find_elements_by_xpath(".//span[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_GridViewResults_LabelLERNum_')]/a").text
                	continue
                # class of variable link is 'selenium.webdriver.remote.webelement.WebElement'
                old = os.path.join(DOWNLOAD_DIR_PATH, accession + ".TXT")
                new = os.path.join(DOWNLOAD_DIR_PATH, ler_number + ".TXT")
                
            	try:
            		os.rename(old, new)
            	except:
            		continue 
            		
            	dload_count += 1
            	print(str(dload_count) + " file(s) changed.")
     
                
            else:
                continue
        # Move on to the next page if there is one
        try:
            next_button = browser.find_elements_by_xpath("//input[contains(@id, 'ContentPlaceHolderMainClientArea_ContentPlaceHolderMainPageContent_ContentPlaceHolderMainPageContent_ImageButtonNext')]")[0]
            next_button.click()
        except:
            break
    print("Changed " + str(dload_count) + " files")

def main():
    query_count = 0
    option = webdriver.ChromeOptions()
    option.add_argument(" - incognito")
    browser = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, chrome_options=option)
    with open(INPUT_FILE_PATH, "r") as f:
        queries = json.load(f)
        for query in queries:
            if search(browser, query):
                name_changer(browser)
                query_count += 1
                print("\n" + str(query_count) + " queries completed!" + "\n")
    browser.quit()

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("Usage: python search.py <search query input file path> <download directory path> <chrome drivr path>")
        exit(1)
    # See expected input file format in README
    INPUT_FILE_PATH = sys.argv[1]
    DOWNLOAD_DIR_PATH = sys.argv[2]
    CHROME_DRIVER_PATH = sys.argv[3]
    main()

'''
def main(folder_1,folder_2):
	i = 0
	for filename in os.listdir(folder_1):
		if filename.startswith('80', 0, 2) or filename.startswith('81', 0, 2) or filename.startswith('82', 0, 2) or filename.startswith('83', 0, 2) or filename.startswith('84', 0, 2):
			i += 1
			old = folder_1 + "/" + filename
			new = folder_2 + "/" + filename
			os.rename(old,new)
			print i 
		else:
			continue 

if __name__ == '__main__':
	main(sys.argv[1],sys.argv[2])
'''
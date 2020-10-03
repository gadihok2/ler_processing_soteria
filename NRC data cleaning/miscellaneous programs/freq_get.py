import os
import csv

os.chdir('/Volumes/Nalin/NSF_data_theoretic/LER downloads and ouputs/ler_numbers/2000-2018')

f = open('out_2007_AO.txt', 'r')
content = f.read()
list_1  = content.split(" ")
freq = {}



count = 0



for i in list_1:
	count+=1
	print(count)
	if count<3000000:
		if i in freq:
			freq[i] += 1
		else:
			freq[i] = 1
	else:
		if i in freq:
			freq[i] += 1
		else:
			continue 

freq_sorted_keys = sorted(freq, key=freq.get, reverse=True)

with open('freq_2007.csv', mode='w') as freq_file:
    freq_writer = csv.writer(freq_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    limit = 1
    for i in freq_sorted_keys:
		limit+=1
		if limit<20001:
			freq_writer.writerow([i, freq[i]])
		else:
			break


'''
import xlwt
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("Sheet 1")
column=0
limit = 1
for i in freq_sorted_keys:
	limit+=1
	if limit<20001:
		sheet1.write(column, 0, i)
		sheet1.write(column, 1, freq[i])
		column += 1
	else:
		break

book.save("freq.xls")
'''
		
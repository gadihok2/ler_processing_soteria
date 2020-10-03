import os
import pandas as pd
import xlrd
import nltk 
from nltk.corpus import words

#INCOMPLETE FILE. TO REMOVE MOST FREQUENT NON-WORDS FROM THE OUTPUT FILE. 

os.chdir('/Volumes/Nalin/NSF_data_theoretic/LER downloads and ouputs/ler_numbers/2000-2018')

file = 'freq_2007.csv'

def read_data( input_file ):
   d = { }
   for line in open( input_file ):
   	try:
   		line = line.rstrip( )
   		line = line.split(',')
   		para = line[0]
   		value = line[1]
   		d[para] =  int(value)
   	except:
   		continue
   return d 

d1 = read_data(file)
d2 = sorted(d1, key=d1.get, reverse=True)




l1 = []
l2 = []
l3 = []
l4 = []

#for i in d1.keys():
	#print i
count = 0
print(len(d2))
for x in d2:
	count += 1
	print(count)
	try:
		if x[0].isupper() == True and x[1].isupper()==False:
			x = x.lower()
	except:
		continue 

	if x in words.words():
		l1.append(x)
	elif x.isupper():
		l2.append(x)
	else:
		l3.append(x)

	if count == 10000:
		break

print(l1)
print('--------------------------------------------')
print(l2)
print('--------------------------------------------')
print(l3)




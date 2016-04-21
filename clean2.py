import csv
import sys
import re
from collections import Counter
#sys.setdefaultencoding("utf-8")
with open('GrossBudgetFinal.csv',encoding = "utf8") as csvfile:
	content = csvfile.readlines()
print(len(content))
count = 0
#content2 = []
regex = r"(\d+),([^\d]{1,5})(\d+),([^\d]{1,5})(\d+)-\((\w+)\)(-.+-|-\()(\d{4})\),(.+)"
#([^\d]{1,5})(\d+)-\((\w+)\)-.+-(\d{4})\),(.+)"
outputcsv = open('outputcsv2.csv','r+',encoding='utf8')
previoustitle = ""
currencies = []
for line in content:
	count = count + 1
	match = re.search(regex,line)
	if(match):
		if((str(match.group(9))!=previoustitle) and (str(match.group(4)) == "$") and (str(match.group(2)) == "$")):
			#print(match.group(1)," ",match.group(2)," ",match.group(3)," ",match.group(4)," ",match.group(5))
			for i in (3,5,6,8):#include 1 in this group to add currency
				outputcsv.write(str(match.group(i))+',')
			outputcsv.write(str(match.group(9))+"\n")
		previoustitle = str(match.group(9))
		currencies.append(str(match.group(4)))
	element = line.split(',')
	#if(count > 20):
	#	break
		#print(element)
	#content2.append(element)
print(count)
uniquecurrencies = set(currencies)
print(Counter(currencies))
print(uniquecurrencies)
outputcsv.close()
	#reader = csv.DictReader(csvfile)
	#for row in reader:
	#	print(row['First'], row['Second'])
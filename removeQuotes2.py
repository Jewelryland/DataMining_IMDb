import os 

fileName=input("enter file name: ")
f1=open(fileName,'r')
f2=open('test.csv','w')
for line in f1:
	line=line.replace('"','')
	line=line.replace(' - ','-')
	line=line.replace(' ','-')
	line=line.replace('\,','')
	line=line.replace('.','')
	f2.write(line)
f1.close()
f2.close()
os.remove(fileName)
os.rename('test.csv',fileName)



ia = imdb.IMDb()
s_result = ia.search_movie('A 3D Guide to Belly Dancing')
for item in s_result:
   print item.movieID

from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True)
imdb = Imdb(cache=True)

f1=open('title.csv','r')
f2=open('details.csv','w')
title=[]
#movieID=[]

for line in f1:
	line=line.strip()
	title.append(line)

for item in title:
	temp = imdb.search_for_title(item)
	for temp_item in temp:
		temp_item = str(temp_item)
		f2.write(temp_item)
		f2.write('\n')
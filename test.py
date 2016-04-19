from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True)
imdb = Imdb(cache=True)

f1=open('titletest.csv','r')
f2=open('popular_shows.csv','w')
title=[]
movieID=[]

for i in imdb.popular_shows():
	i=str(i)
	f2.write(i)
	f2.write('\n')

'''
for line in f1:
	line=line.strip()
	title.append(line)

for item in title:
	if(imdb.title_exists(item)):
		print item.title, item.rating
	else:
		continue
'''
'''for i in range(0, len(title)):
	f2.write(title[i])
	f2.write(',')
	f2.write(movieID[i])
	f2.write('\n')
'''

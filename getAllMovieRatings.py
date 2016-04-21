#based off details.csv from getAllMovieDetails.py

#ONLY SOME MOVIES WILL BE WRITTEN INTO F2. cOPY THEM INTO TEMPmOVIErATINGS. kEEP DOING THIS

from imdbpie import Imdb
imdb = Imdb()
imdb = Imdb(anonymize=True)
imdb = Imdb(cache=True)

f1=open('Details.csv','r')
f2=open('movieRatings.csv','w')
movieID=[]
year=[]
count=1 #just to show how much is written in new file

for line in f1:
	attribute=line.split(",") #splitting each item
	attribute[-1]=attribute[-1].strip() #removing \n from the last attribute
	#year.append(attribute[0]) #storing only years
	movieID.append(attribute[1])#storing only movie ids

for item in movieID:
	if(imdb.get_title_by_id(item)): #checking if movie exists
		print(count)
		title=imdb.get_title_by_id(item)
		rating=str(title.rating)
		if(rating is "None"):
			f2.write("None")
		else:
			f2.write(rating)
		f2.write(',') #so that it's in csv format

		year=str(title.year)
		if(year is "None"):
			f2.write("None")
		else:
			f2.write(year)
		f2.write(',')
		
		title=str(title)
		f2.write(title)
		f2.write('\n')
		count = count+1
	else:
		continue
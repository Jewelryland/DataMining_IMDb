from collections import Counter
from string import punctuation
import nltk;

def content_text(text):
    stopwords = set(nltk.corpus.stopwords.words('english')) # 0(1) lookups
    with_stp = Counter()
    without_stp  = Counter()
    with open(text, encoding='utf8') as f: #change encoding to UTF 8 if reading from charName2
        for line in f:
            spl = line.split()
            # update count of all words in the line that are in stopwrods
            with_stp.update(w.lower().rstrip(punctuation) for w in spl if w.lower() in stopwords)
               # update count of all words in the line that are not in stopwords
            without_stp.update(w.lower().rstrip(punctuation)  for w in spl if w  not in stopwords)
    # return a list with top hundred most common words from each 
    return [x for x in with_stp.most_common(200)],[y for y in without_stp.most_common(200)]
#wth_stop, wthout_stop = content_text('titleYear.csv')

wth_stop, wthout_stop = content_text('charName2.csv')
words = open('words.txt','r+',encoding='utf8')
print(type(wthout_stop))
words.write('\n'.join('%s %s' % x for x in wthout_stop))

words.close()
#result = content_text('titleYear.csv')
print(wth_stop)
print("-------------------------------------------------")
print(wthout_stop)
from nltk.book import text6
n=len(text6)       '''returns number of words in text  16967'''
u=len(set(text6))   '''returns unqiue words            - 2166'''
wc = n/u             '''word covergae                  - 7.8333'''

ise_ending_words = [word for word in set(text6) if word.endswith('ise') ]        '''4''' 
n_ise = len(ise_ending_words)

containz_z = [word for word in set(text6) if 'z' in word]
print(len(contain_z))                                                             '''8'''

title_words = [word for word in text6 if (len(word)==1 and word[0].isupper()) or (word[0].isupper() and word[1:].islower()) ]
print(len(title_words))

text6_freq_words = [word for word in text6 if word.isalpha()  ]
text6_freq = nltk.FreqDist(text6_freq_words)

text6_freq_ar = nltk.FreqDist(text6)
text6_freq_ar['ARTHUR']

from nltk.corpus import gutenberg
gutenberg.fileids()
for fileid in gutenberg.fileids():
    total_unique_words = len(set(gutenberg.words(fileid)))
    total_words = len(gutenberg.words(fileid))
    print(total_words/total_unique_words,fileid)
  
  from nltk.corpus import brown
  brown_cfd = nltk.ConditionalFreqDist([ (genre, word.lower()) for genre in brown.categories() for word in brown.words(categories=genre) ])
  brown_cfd.tabulate(conditions = ['news','religion','romance'],samples = ['can', 'could', 'may', 'might', 'must', 'will'])
  
  
  from nltk.corpus import inaugural
  cfd = nltk.ConditionalFreqDist(
...           (target, fileid[:4])
...           for fileid in inaugural.fileids()
...           for w in inaugural.words(fileid)
...           for target in ['america', 'citizen']
...           if w.lower().startswith(target))

from urllib import request
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/Python_(programming_language"
html_content = request.urlopen(url).read()
soup = BeautifulSoup(html_content, 'html.parser')

n_links = [item['href'] for item in soup.select('.reflist a')]
print(len(n_links))

import nltk
from nltk.corpus import brown
from nltk.corpus import stopwords
news_words     = brown.words(categories='news')
lc_news_words  = [l.lower() for l in news_words]
len_news_words = [len(w) for w in lc_news_words]
news_len_bigrams = list(nltk.bigrams(len_news_words))
cfd_news      = nltk.ConditionalFreqDist(news_len_bigrams)
cfd_news.tabulate(conditions=[6,4])

lc_news_bigrams = list(nltk.bigrams(lc_news_words))
lc_news_alpha_bigrams = [(w1,w2) for w1,w2 in lc_news_bigrams if (w1.isalpha() and w2.isalpha())]
stop_words = stopwords.words()
lc_stop_words = [l.lower() for l in stop_words]
lc_news_alpha_nonstop_bigrams = [ (w1, w2) for w1, w2 in lc_news_alpha_bigrams if (w1.lower() not in lc_stop_words and w2.lower() not in lc_stop_words) ]
print(len((lc_news_alpha_nonstop_bigrams)))


import nltk
import nltk.corpus
from nltk.corpus import brown
humor_words = brown.words(categories = 'humor')
lc_humor_words = [w.lower() for w in humor_words]
lc_humor_uniq_words = set(lc_humor_words)
from nltk.corpus import words
wordlist_words = words.words()
wordlist_uniq_words = set(wordlist_words)
from nltk.stem import PorterStemmer
porter = PorterStemmer()
from nltk.stem import LancasterStemmer
lancaster = LancasterStemmer()
p_stemmed = []
for word in lc_humor_uniq_words:
    p_stemmed.append(porter.stem(word))
l_stemmed = []
for wordd in lc_humor_uniq_words:
    l_stemmed.append(lancaster.stem(wordd))
p_stemmed_in_wordlist = [word1 for word1 in p_stemmed if word1 in wordlist_uniq_words]
l_stemmed_in_wordlist = [word2 for word2 in l_stemmed if word2 in wordlist_uniq_words]
p_stemmed_diff=[]
for w1,w2 in zip(lc_humor_uniq_words,p_stemmed):
    if len(w1) == len(w2) and w1 != w2:
        p_stemmed_diff.append(w1)
l_stemmed_diff=[]
for w1,w2 in zip(lc_humor_uniq_words,l_stemmed):
    if len(w1) == len(w2) and w1 != w2:
        l_stemmed_diff.append(w1)
print(len(p_stemmed_diff))
print(len(l_stemmed_diff))

lc_humor_uniq_words = list(lc_humor_uniq_words)
k = 0
p_stemmed_diff = []
for w1 in lc_humor_uniq_words:
   for i in range(k,len(p_stemmed)):
      if len(w1) == len(p_stemmed[i]) and w1 != (p_stemmed[i]):
         p_stemmed_diff.append(w1)
      k = k + 1
      break
print(len(p_stemmed_diff))


l = 0
l_stemmed_diff = []
for w2 in lc_humor_uniq_words:
   for j in range(l,len(l_stemmed)):
       if len(w2) == len(l_stemmed[j]) and w2 != (l_stemmed[j]):
          l_stemmed_diff.append(w2)
       l = l + 1
       break
print(len(l_stemmed_diff))

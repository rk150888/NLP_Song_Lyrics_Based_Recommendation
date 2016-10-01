# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 15:52:00 2016

"""

import nltk

f = open("/home/rohit/Downloads/Data_Dipankar_SPJain.txt")
raw = f.read().encode('utf8')
len(raw)
from nltk.corpus import wordnet as wn


# remove stopwords
from nltk.corpus import stopwords
stop = set(stopwords.words('english'))
words=[i for i in raw.lower().split() if i not in stop]
print(words)
len(words)

# unique words
uny=[]
unique_words = set(words)
for word in unique_words:
    uny.append(str(word))
len(uny)

#[w for w in uny if w=="sathe"]

import sys  

reload(sys)  
sys.setdefaultencoding('utf8')


## identify word as english/non-english
dict={}
import enchant
d=enchant.Dict("en_GB")
i=0
for word in uny:
    lst = []
      
    if d.check(unicode(word, "utf-8", errors='replace')):
        for synset in wordnet.synsets(word):
            l = synset.name().partition('.')
            lst.append([str(l[0]),str(l[2])])
        dict[word]=lst
        
        
       
a=open("/home/rohit/Desktop/output.txt","w")
def write_report(r, filename):
    input_file=open(filename, "a")
    for k, v in r.items():
        line = '{}, {}'.format(k, v) 
        print(line, file==input_file)        
    
 

import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from nltk.stem import PorterStemmer
import numpy as np
np.random.seed(2018)

porter=PorterStemmer()
import nltk
nltk.download('wordnet')

import pandas as pd
data = pd.read_csv('google_querie5.csv', error_bad_lines=False);
data_text = data[['query']]
data_text['index'] = data_text.index
documents = data_text
import pandas as pd
data1 = pd.read_csv('stopwords2.csv', error_bad_lines=False);
data_stop = data1['words']
data_stop1=[]
for i in data_stop:
    data_stop1.append(i)
    
def lemmatize_stemming(text):
    return porter.stem(WordNetLemmatizer().lemmatize(text, pos='v'))
def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        token=lemmatize_stemming(token)
        if token not in data_stop1:
            result.append(token)
    return result

processed_docs = documents['query'].map(preprocess)
dictionary_google = gensim.corpora.Dictionary(processed_docs[0:100])
dictionary_ubereats = gensim.corpora.Dictionary(processed_docs[100:200])
dictionary_uber = gensim.corpora.Dictionary(processed_docs[200:300])
count = 0
list_google=[]
for k, v in dictionary_google.iteritems():
    list_google.append(v)
    
list_ubereats=[]
for k, v in dictionary_ubereats.iteritems():
    list_ubereats.append(v)
    
list_uber=[]
for k, v in dictionary_uber.iteritems():
    list_uber.append(v)
    
    
count_google=len(list_google)
count_uber=len(list_uber)
count_ubereats=len(list_ubereats)

dict_google={}
for k in list_google:
    dict_google[k]=0
    for query1 in processed_docs[0:100]:
        if k in query1:
            dict_google[k]+=1
    dict_google[k]=dict_google[k]/count_google
import csv

dict_ubereats={}
for k in list_ubereats:
    dict_ubereats[k]=0
    for query1 in processed_docs[100:200]:
        if k in query1:
            dict_ubereats[k]+=1
    dict_ubereats[k]=dict_ubereats[k]/count_ubereats
            
            
dict_uber={}
for k in list_uber:
    dict_uber[k]=0
    for query1 in processed_docs[200:300]:
        if k in query1:
            dict_uber[k]+=1
    dict_uber[k]=dict_uber[k]/count_uber
    
google_file=pd.DataFrame.from_dict(dict_google, orient='index',columns=['probability'])
google_file.to_csv('google_queries_prob.csv', sep=',', encoding='utf-8')

uber_file=pd.DataFrame.from_dict(dict_uber, orient='index',columns=['probability'])
uber_file.to_csv('uber_queries_prob.csv', sep=',', encoding='utf-8')

ubereats_file=pd.DataFrame.from_dict(dict_ubereats, orient='index',columns=['probability'])
ubereats_file.to_csv('ubereats_queries_prob.csv', sep=',', encoding='utf-8')
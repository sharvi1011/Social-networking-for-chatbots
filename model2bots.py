import socket
import gensim
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer, SnowballStemmer
from nltk.stem.porter import *
from nltk.stem import PorterStemmer
import numpy as np
import pandas as pd

def lemmatize_stemming(text):
    ps = PorterStemmer()
    text=WordNetLemmatizer().lemmatize(text, pos='v')
    return ps.stem(text)
def preprocess(text,data_stop1):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        token=lemmatize_stemming(token)
        if token not in data_stop1:
            result.append(token)
    return result




def Main():

    
    print('import done')

    data1 = pd.read_csv('stopwords2.csv', error_bad_lines=False);
    data_stop = data1['words']
    data_stop1=[]
    for i in data_stop:
        data_stop1.append(i)

    print('stopwords done')


    np.random.seed(2018)

    data = pd.read_csv('google_queries_prob1.csv', error_bad_lines=False);
    dict_google={}
    for i in range(0,data.count()['query']):
        dict_google[data['query'][i]]=data['probability'][i]

    print('google done')

    data = pd.read_csv('uber_queries_prob1.csv', error_bad_lines=False);
    dict_uber={}
    for i in range(0,data.count()['query']):
        dict_uber[data['query'][i]]=data['probability'][i]

    print('uber done')

    data = pd.read_csv('ubereats_queries_prob1.csv', error_bad_lines=False);
    dict_ubereats={}
    for i in range(0,data.count()['query']):
        dict_ubereats[data['query'][i]]=data['probability'][i]

    data = pd.read_csv('ip_addr.csv', error_bad_lines=False);
    dict_ip={}
    for i in range(0,data.count()['chatbot']):
        dict_ip[data['chatbot'][i]]=data['ip_address'][i]


    print('ubereats done')
    
    host_client = '192.168.0.106'
    port_client = 5000

    s_client = socket.socket()  #socket for client
    s_client.bind((host_client,port_client))    #binding socket

    s_client.listen(1)
    print('listening from client')
    client, addr = s_client.accept()
    print(addr)
    print(type(addr))
    print("Connection from: " + str(addr))
    while True:
        query = client.recv(1024).decode('utf-8')    #receiving from client
        if query:
            print("from connected user: " + query)

            result_google=0
            result_ubereats=0
            result_uber=0
            for i in preprocess(query,data_stop1):
                if i in dict_google.keys():
                    result_google+=dict_google[i]
                if i in dict_ubereats.keys():
                    result_ubereats+=dict_ubereats[i]
                if i in dict_uber.keys():
                    result_uber+=dict_uber[i]
            company_dict={'google':result_google,'uber':result_uber,'ubereats':result_ubereats}
            result_value=max(company_dict.values())

            print (list(company_dict.keys())[list(company_dict.values()).index(result_value)])
            result=list(company_dict.keys())[list(company_dict.values()).index(result_value)]
            
            print("sending: " + result)
            ip_addr=dict_ip[result]
            ip_addr='192.168.0.105'
            print('ip address: ',ip_addr)
            
            client.send(ip_addr.encode('utf-8'))       #sending client
            break
    client.close()
    print('client close')                      #closing connection

if __name__ == '__main__':
    Main()
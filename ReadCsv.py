from numpy import genfromtxt,recfromcsv
import csv
from textblob import TextBlob
from nltk.tokenize import TweetTokenizer
from langdetect import detect
import numpy as np
with open('elonmusk_tweets.csv','r') as dest_f:
    data_iter = csv.reader(dest_f,
                           delimiter = ',',
                           quotechar = '"')

    data = [data for data in data_iter]
tweets=[]
for val in data:

    tt=val[2].strip('b')
    tt=tt.strip('"')
    tt=tt.strip("'")
    tweets.append(tt)

print(tweets)
tok=TweetTokenizer()
listTw=[]
for tweet in tweets[1:]:
    some=tok.tokenize(tweet)
    #print(some)
    sen=""
    for w in some:

        if not w.isalpha():
            sen=sen+""

        else:
            sen=sen+w.lower()+" "
    #print(sen)

    if len(sen)>0:
        lang=detect(sen)
        sen=sen+"\n"
        if lang == 'en':
            listTw.append(sen)

with open('tweets.txt', 'w') as f:
    f.writelines(listTw)


from nltk.tokenize import TweetTokenizer
from langdetect import detect
tweets=[]
labels=[]
listTw={}
tok=TweetTokenizer()
with open('Manually-Annotated-Tweets.tsv','r') as f:
    for x in f.readlines():
        p=x.split("\t")
        #print(x)
        #print(p)



        some=tok.tokenize(p[0])
        #print(some)
        sen=""
        for w in some:

            if not w.isalpha():
                sen=sen+""

            else:
                sen=sen+w.lower()+" "
        print(sen)

        if len(sen)>0:
            lang=detect(sen)
            sen=sen+"\n"
            if lang == 'en':
                listTw[sen.strip('\n')]=p[1].strip('\n')

with open('twitter.txt','w') as f:
    for k,v in listTw.items():
        f.write(k+":"+v+'\n')

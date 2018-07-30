import urllib3
from bs4 import BeautifulSoup
from nltk import WordNetLemmatizer
#from textblob import Word
PosiwordList={}
NegeWordList={}

def get_label(word,senti):
    word=str(word)
    word=word.lower()
    word=word.strip()
    #print(word)
    if senti is 'pos':
        PosiwordList[word]=+1
    elif senti is 'neg':
        NegeWordList[word]=-1
def WordList(url,senti):
    http=urllib3.PoolManager()
    r=http.request('GET',url)
    print(r.status)
    #print(r.data)
    soup=BeautifulSoup(r.data,'html.parser')
    #h2=soup.find_all('h2')
    #print(h2[0])
    for h2 in soup.find_all('p'):

        some=(h2.text)
        #print(some)
        for word in some.split(","):
            if word.isupper():
                print(word)
                wordNew=set(word)
                #print(wordNew)
                if '–' in wordNew:
                    #print("enter")
                    s=word.split('–')
                    for f in s:
                        get_label(f,senti)
                else:
                    get_label(word,senti)


WordList("http://positivewordsresearch.com/list-of-positive-words/",'pos')
#WordList("http://positivewordsresearch.com/list-of-negative-words/",'neg')
print(PosiwordList)
print(NegeWordList)
def NegWordList(url,senti):
    http=urllib3.PoolManager()
    r=http.request('GET',url)
    print(r.status)
    #print(r.data)
    soup=BeautifulSoup(r.data,'html.parser')
    #h2=soup.find_all('h2')
    #print(h2[0])
    for h2 in soup.find_all('p'):

        some=(h2.text)
        #print(some)
        for word in some.split(","):
            #print(word)
            if len(word.split())<3:
                wordNew=set(word)
                #print(wordNew)
                if '–' in wordNew:
                    #print("enter")
                    s=word.split('–')
                    for f in s:
                        get_label(f,senti)
                else:
                    get_label(word,senti)
NegWordList("http://positivewordsresearch.com/list-of-negative-words/",'neg')
print(NegeWordList)
lem=WordNetLemmatizer()
posi={}
for word,wt in PosiwordList.items():
    try:
        word=lem.lemmatize(word)
    except:
        pass
    try:
        word = lem.lemmatize(word,'v')
    except:
        pass
    posi[word]=wt
nege={}
for word,wt in NegeWordList.items():
    try:
        word=lem.lemmatize(word)
    except:
        pass
    try:
        word = lem.lemmatize(word,'v')
    except:
        pass
    nege[word]=wt
print(posi)
print(nege)
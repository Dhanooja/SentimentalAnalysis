from textblob import TextBlob
lst=[]
with open('Adverb.txt','r') as f:
    for i in f.readlines():
      word=i.strip('\n')
      text=TextBlob(word)
      print(word,text.sentiment.polarity)
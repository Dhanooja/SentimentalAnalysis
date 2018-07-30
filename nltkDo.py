from textblob import TextBlob
text="the woman is walking slowly"
text=TextBlob(text)
print(text.sentiment.polarity)
x=text.sentences
for v in x:
    v=TextBlob(str(v))
    print(v.tags)
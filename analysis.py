import softComputing
#import sp
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
another=0

with open('twitter.txt','r') as f:
    counthere=0
    my_hit=0
    my_miss=0
    nltk_hit=0
    nltk_miss=0
    for p in f.readlines()[:1000]:
        #print(labels[counthere])
        p=p.strip('\n')
        p=p.split(":")
        x=str(p[0])
        print(x,p[1])
        my_rslt=None
        try:
            total=softComputing.rate(x)
            val=softComputing.review(total)
            print(max(val,key=val.get))
            my_rslt=max(val,key=val.get)
        except:
            pass
        ana=SentimentIntensityAnalyzer()
        nltk_ana=ana.polarity_scores(x)
        print(nltk_ana)
        print(max(nltk_ana, key=nltk_ana.get))
        nltk_rslt=max(nltk_ana, key=nltk_ana.get)
        if my_rslt is not None:
            if my_rslt =='pos:' and p[1] =='positive':
               my_hit+=1
            elif my_rslt == 'neg:' and p[1] == 'negative':
                my_hit+=1
            elif my_rslt == 'neu:' and p[1] == 'objmspam':
                my_hit+=1
            elif my_rslt == 'vague:' and p[1] == 'objspam':
                my_hit+=1
            else:
                my_miss+=1
        if nltk_rslt is not None:
            if nltk_rslt == 'pos' and p[1] == 'positive':
                nltk_hit += 1
            elif nltk_rslt == 'neg' and p[1] == 'negative':
                nltk_hit += 1
            elif nltk_rslt == 'neu' and p[1] == 'objmspam':
                nltk_hit += 1
            elif nltk_rslt == 'compound' and p[1] == 'objspam':
                nltk_hit += 1
            else:
                nltk_miss += 1
        counthere+=1


print(my_hit,my_miss,counthere)
print(nltk_hit,nltk_miss,counthere)
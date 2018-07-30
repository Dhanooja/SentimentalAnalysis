count=0

def rate(string):
    global count
    dicti = {}
    with open('test.txt', 'r') as f:
        for l in f.readlines():
            key, val = l.split(":")
            dicti[key] = int(val)

    with open('Adverb.txt', 'r') as f:
        for l in f.readlines():
            l=l.strip('\n')
            if l in dicti:
                pass
            else:
                dicti[l] = 0
    extra={'not':-.5,'wish':2,'super':2,'never':-2,'no':-2,'very':+2,'awfully':-2,"don't":-2,"won't":-2,"couldn't":-2,"wouldn't":-2,"shouldn't":-2,}
    exitwords = {'can','may','must','could', 'would', 'been', 'have', 'might', 'may'}
    #string= str(input("enter comment"))
    reveiw= string.lower().split()
    total=0
    flag=0
    #print(reveiw)
    reveiw=clean(reveiw)
    #print(reveiw)
    for val in reveiw:

        thisindex = reveiw.index(val)

        # print(thisindex)
        if val in extra:

            for i in range(thisindex,len(reveiw)):
                if reveiw[i] in dicti:
                    #print(reveiw[i])
                    total=total+(dicti.get(reveiw[i])*extra.get(val))
                    reveiw[i]='0'
                    #print("in extra",total)
                    #print("------------")
                    #print()
                    break

        elif val in dicti:
            total=total+dicti.get(val)
            #print(dicti.get(val))
            #print("in dicti",val, total)
        elif val in exitwords:
            if reveiw[thisindex+1] in exitwords:
                for i in range(thisindex,len(reveiw)):
                    if reveiw[i] in dicti:
                        reveiw[i]='0'
                        break
            #print("in exit", val,total)
        reveiw[thisindex]='0'
        if val in dicti:
            count+=1
            #print(val)
        #print(reveiw)
    #print(total)
    return total
#cleaning the review
#from textblob import Word
from nltk import WordNetLemmatizer
def clean(word_list):
    lem=WordNetLemmatizer()
    cleanlist = []
    for word in word_list:
        symbols = "!@~#$%^&*()_+=-<>?:{}[];',./"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], "")  # replace those symbols with nothing

        if len(word) > 0:
            #print(word)

            word=lem.lemmatize(word,'v')

            cleanlist.append(word)
    return cleanlist

def review(total):
    global count
    rev={'pos:':0,'neg:':0,'neu:':0,'vague:':0}
    if total>0:
        print("Positive Review")
        rev['pos:']=1
    elif total<0:
        print("Negetive review")
        rev['neg:']=1
    elif total==0 and count>0:
        print("Neutral review")
        rev['neu:']=1
    elif count==0:
        print("This is a vague review.....Cannot be considered!!!!!!!!!!!")
        rev['vague:']=1
    print(rev)

    count=0
    return rev

#Input The data
#print("enter any review:")
#rev="it was the best movie since citizen kane"
#total=rate(rev)
#print(total)
#review(total)


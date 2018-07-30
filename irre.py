from nltk import WordNetLemmatizer
from textblob import Word
lem=WordNetLemmatizer()
word=lem.lemmatize("purest")
print(word)
word=Word("purest")
print(word.lemmatize())
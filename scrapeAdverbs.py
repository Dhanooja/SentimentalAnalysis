import urllib3
from bs4 import BeautifulSoup

http=urllib3.PoolManager()
r=http.request('GET','https://positivethesaurus.com/list-of-positive-adverbs-a-to-z/')
soup=BeautifulSoup(r.data,'html.parser')
listPosi=[]
for para in soup.find_all('p'):
  #  print(para.text)
    some=para.text.split("\n")
 #   print(some)
    for w in some:
        listPosi.append(w.lower())
#print(listPosi)

for i in range(1,len(listPosi)):
    listPosi[i-1]=listPosi[i]
#print(listPosi)

with open('Adverb.txt','w') as f:
    for i in listPosi:
        f.write(str(i+'\n'))
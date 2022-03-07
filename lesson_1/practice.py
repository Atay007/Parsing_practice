import requests

from bs4 import BeautifulSoup

url=requests.get('https://globus-online.kg/catalog/myaso_ptitsa_ryba/govyadina_baranina_farshi/')
html=BeautifulSoup(url.content,'html.parser')

# item=html.select('#view-showcase > #bx_3966226736_199728 > .list-showcase__part-main > .list-showcase__name-rating')

# items=html.select('.gopro-container > .list-showcase')
# for i in items:
#     name=i.select('.js-element > .list-showcase__name > a')
#     file=open('parsing.txt','a+',encoding='utf-8')
#     print(name[0].text)
#     file.write(f'{name[0].text}\n')
#     file.close()

data_name=html.find_all(class_="list-showcase__name")
data_prize=html.find_all(class_="c-prices__value")


dct={}
lst=[]
b=0

for i in data_name:
    dct[i.text]=b

for j in data_prize:
    lst.append(j.text)

for k in dct:
    dct[k]=lst[b]
    b+=1
print(dct)

with open('parsing/parse.txt','w',encoding='utf-8') as file:
    for k,v in dct.items():
        file.write(f'{k}, prise: {v}\n')
file.close()

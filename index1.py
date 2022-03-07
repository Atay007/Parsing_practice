from re import T
import requests
from bs4 import BeautifulSoup
# link='http://icanhazip.com/'
# print(requests.get(link).text)

#################################
# req=requests.get('https://stopgame.ru/review/new/stopchoice')
# html=BeautifulSoup(req.content,'html.parser')

# for el in html.select('.items > .article-summary'):
#     title=el.select('.caption > a')
#     print(title[0].text)
################################
# req=requests.get('https://stopgame.ru/review/new/stopchoice')
# html=BeautifulSoup(req.content,'html.parser')

# with open('parsing/text.txt','w', encoding='utf-8') as file:
#     for i in html.select('.items > .article-summary'):
#         pict=i.select('.caption > a')
#         file.write(str(f'{pict[0]}\n'))
# file.close()
########################
page=1
while True:
    req=requests.get('https://stopgame.ru/review/new/stopchoice/p'+str(page))
    html=BeautifulSoup(req.content,'html.parser')
    items = html.select('.items > .article-summary')
    if len(items):
        for i in items:
            title = i.select('.caption > a')
            file=open('parsing/text.txt','a+',encoding='utf-8')
            file.write(f'{title[0].text}\n')
            file.close()
            print(title[0].text)
        page+=1
    else:
        break
    



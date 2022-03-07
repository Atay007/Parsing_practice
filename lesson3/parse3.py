import requests

from bs4 import BeautifulSoup as bs
import json

link='https://quote.rbc.ru/'
headrs={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

req=requests.get(link,headers=headrs)

# with open('parsing/lesson3/quote.html','w',encoding='utf-8') as file:
#     file.write(req.text)
#     file.close()
with open('parsing/lesson3/quote.html','r',encoding='utf-8') as file:
    src=file.read()
    file.close()
soup=bs(src,'lxml')
all_invest=soup.find_all(class_='q-item__wrap')
catalog={}

for item in all_invest:
    title=item.find(class_='q-item__title')
    item_link=item.find('a')
    item_href=item_link.get('href')
    catalog[title]=item_link

print(catalog)
with open('parsing/lesson3/catalog.json','w',encoding='utf-8') as file:
    json.dump(catalog,file,indent=4, ensure_ascii=False)


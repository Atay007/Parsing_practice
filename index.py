import requests
from bs4 import BeautifulSoup as bs
import json

header={
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


for i in range(2,9):
    #Берем сылку и читаем содержимое
    url=f'https://shop.casio.ru/catalog/?PAGEN_1={i}'
    req=requests.get(url,headers=header)
    response=req.content

    # Находим Название модели цену и ссылку класса
    soup=bs(response,'lxml')

    articles=soup.find_all('p',class_='product-item__articul')
    links=soup.find_all('a',class_='product-item__link')
    prize=soup.find_all(class_='product-item__price')

    # создаем переменые итерируемся по ценам и моделям и добавляем в список
    lst_artic=[]
    lst_prize=[]

    for j in prize:
        lst_prize.append(j.text.strip())

    for x in articles:
        lst_artic.append(x.text.strip())
    
    # создаем переменую что бы итерируваться по индексам модели и ценам
    c=0

    for item in links:
        a_href='https://shop.casio.ru/'+str(item.get('href').strip())# Берем ссылки модели
        dct={
            'Model': lst_artic[c],
            'Prize':lst_prize[c],
            'Link': a_href
        }
        c+=1

    with open('parsing/casio1/watch_casio.json','a',encoding='utf-8') as file:
        json.dump(dct,file,indent=4,ensure_ascii=False)
    







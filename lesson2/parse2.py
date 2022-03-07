import requests

from bs4 import BeautifulSoup as Bs

import json
import csv

url='https://health-diet.ru/table_calorie/'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}

req=requests.get(url,headers=headers)
with open('parsing/lesson2/diet.html','w',encoding='utf-8') as file:
    file.write(req.text)

with open('parsing/lesson2/diet.html','r',encoding='utf-8') as file:
    src=file.read()

soup=Bs(src,'lxml')
all_products_hrefs=soup.find_all(class_='mzr-tc-group-item-href')
print(all_products_hrefs)
all_categories={}

for item in all_products_hrefs:
    item_text=item.text
    item_href='http://health-diet.ru'+item.get('href')
    all_categories[item_text]=item_href
print(all_categories)
with open('parsing/lesson2/all_categories.json','w',encoding='utf-8') as file:
    json.dump(all_categories,file,indent=4, ensure_ascii=False)

rep=[',','.',' ','-','\'']

for category_name,category_href in all_categories.items():
    for item in rep:
        category_name=category_name.replace(item,' ')

    req=requests.get(url=category_href,headers=headers)
    src=req.text
    # with open(f'parsing/lesson2/html/{category_name}.html','w',encoding='utf-8') as file:
    #         file.write(src)
    with open(f'parsing/lesson2/html/{category_name}.html','r',encoding='utf-8') as file:
        src=file.read()
        soup=Bs(src,'lxml')

        #собираем заголовки
        table_head=soup.find(class_='mzr-tc-group-table').find(class_='tr').find_all('th')
        product=table_head[0].text
        calories=table_head[1].text
        protein=table_head[2].text
        fats=table_head[3].text
        carbohydrates=table_head[4].text

        with open(f'parsing/lesson2/csv/{category_name}.csv','w',encoding='utf-8') as file:
            writer=csv.writer(file)
            writer.writerow(
                (
                    product,
                    calories,
                    protein,
                    fats,
                    carbohydrates
                )
            )
        #даныые продуктов
        product_data=soup.find(class_='mzr-tc-group-table').find('tbody').find_all('tr')
        for item in product_data:
            product_tdc=item.find_all('td')

            product=product_tdc[0].find('a').text
            calories=product_tdc[1].text
            protein=product_tdc[2].text
            fats=product_tdc[3].text
            carbohydrates=product_tdc[4].text
            # with open(f'parsing/lesson2/csv/{category_name}.csv','w',encoding='utf-8') as file:
            #     writer=csv.writer(file)
            #     writer.writerow(
            #         (
            #             product,
            #             calories,
            #             protein,
            #             fats,
            #             carbohydrates
            #         )
            #     )

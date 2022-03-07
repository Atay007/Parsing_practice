import os
import requests
from bs4 import BeautifulSoup as bs

link1='https://akipress.org/'

header={
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'
}
req=requests.get(link1,headers=header)

    #Записали в файл
    # with open('parsing/AkiExpress/web.html','w',encoding='utf-8') as file:
    #     file.write(req.text)
    #     file.close()

    #Читаем файл
with open('parsing/AkiExpress/web.html','r',encoding='utf-8') as file:
    src=file.read()
    file.close()
soup=bs(src,'lxml')

news=soup.find_all(class_='newslink')

    #Список новостей
    # with open('parsing/AkiExpress/news_list.txt','w',encoding='utf-8') as file:
    #     for i in news:
    #         a='https:'+str(i.get('href'))
    #         file.write(f'{i.text}:{a}\n')
    # file.close()

    # #Добавление в словарь
post={}
for i in news:
    a='https:'+str(i.get('href'))
    post[i.text]=a

    #Вывод общую информацию
for title,link2 in post.items():

    req=requests.get(link2,headers=header)

        # with open(f'parsing/AkiExpress/news_doc/{title}.html','w',encoding='utf-8') as file:
        #     file.write(req.text)

        # with open(f'parsing/AkiExpress/news_doc/{title}.html','r',encoding='utf-8') as file:
        #     src=file.read()

    soup=bs(req.text,'lxml')
    news=soup.find_all('p')

    istory=' '
    for i in news:
        istory+=f'{i.text}\n'

    with open(f'parsing/AkiExpress/news_doc/{title}.txt','w',encoding='utf-8') as file:
        file.write(istory)
        # path=f'parsing/AkiExpress/news_doc/{title}.html'
        # os.remove(path)



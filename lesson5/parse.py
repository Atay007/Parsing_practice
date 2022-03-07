import requests 
from bs4 import BeautifulSoup as bs
import json

# person_url_lst=[]


# for i in range(0,200,20):
#     url=f'https://www.bundestag.de/ajax/filterlist/en/members/453158-453158?limit=20&noFilterSet=true&offset={i}'

#     q=requests.get(url)
#     result=q.content
#     soup=bs(result,'lxml')

#     person=soup.find_all(class_='bt-open-in-overlay')


#     for i in person:
#         person_page_url=i.get('href')
#         person_url_lst.append(person_page_url)

# with open('parsing/lesson5/person_list.txt','w',encoding='utf-8') as file:
#     for line in person_url_lst:
#         file.write(f'{line}\n')

data=[]
with open('parsing/lesson5/person_list.txt','r',encoding='utf-8') as file:
    lines=[line.strip() for line in file.readlines()]

    data_dct={}
    person_dct={}
    link_dct={}

    for line in lines[:2]:
        q=requests.get(line)
        result=q.content
        soup=bs(result,'lxml')

        person=soup.find(class_='bt-biografie-name').find('h3').text
        person_name_company=person.strip().split(',')
        person_name=person_name_company[0]
        person_company=person_name_company[1]
        print(line)

        links=soup.find_all(class_='bt-link-extern')
        for item in links:
            social_url=item.get('href').strip()
            call=item.text.strip()
            link_dct[call]=social_url
    
        data_dct={
            'Person name: ':person_name,
            'Person company': person_company,
            'Social network':link_dct
        }
        data.append(data_dct)
    print(data)
    
    with open('parsing/lesson5/data.json','w',encoding='utf-8') as file:
        json.dump(data,file,indent=4,ensure_ascii=False)

        

    
import requests

link = 'https://browser-info.ru/'
res = requests.get(link).text 
with open('lesson_1/browser.html', 'w', encoding='utf-8') as file:
    file.write(res)
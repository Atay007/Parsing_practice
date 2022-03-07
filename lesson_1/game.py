import requests
from bs4 import BeautifulSoup 

page = 1
while True:
    req = requests.get('https://stopgame.ru/review/new/stopchoice/p'+str(page))
    html = BeautifulSoup(req.content, 'html.parser')
    items = html.select('.items > .article-summary')

    if len(items):
        for el in items:
            title = el.select('.caption > a')
            print(title[0].text)
            file = open('lesson_1/game.txt', 'a+', encoding='utf-8')
            file.write(f"{title[0].text}\n")
            file.close()
        page += 1
    else:
        break

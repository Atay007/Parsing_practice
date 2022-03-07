import requests

link = 'https://icanhazip.com/'
print(requests.get(link).text)
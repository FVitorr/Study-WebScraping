from urllib import response
import requests
from bs4 import BeautifulSoup

class search:
    def __init__(self,url):
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text , 'html.parser')
            with open('file.html','w',encoding="utf-8") as arq:
                arq.write(str(soup.prettify()))
            #print(soup)

        else:
            print(f'Erro Code: {response.status_code}')

search('https://zonadatec.blogspot.com/')
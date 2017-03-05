from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://en.wikipedia.org/wiki/Kevin_Bacon')
bsObj = BeautifulSoup(html, 'html.parser')

#links = bsObj.findAll('a')
for link in bsObj.findAll('a'):
    if 'href' in link.attrs:
        print(link['href'])

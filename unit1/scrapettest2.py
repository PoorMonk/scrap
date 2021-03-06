from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as e:
        return None

    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

url = 'http://www.pythonscraping.com/pages/page1.html'
title = getTitle(url)
if title == None:
    print('Titile could not be found.')
else:
    print(title)

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')

print('-----')
spans = bsObj.findAll(lambda tag: len(tag.attrs) == 2)
for span in spans:
    print(span)

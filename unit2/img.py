from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('https://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html.parser')

imgLists = bsObj.findAll('img', {'src':re.compile('\.\.\/img\/gifts\/img[0-9]+\.jpg')})
for img in imgLists:
    print(img['src'])

print('-'*24)
blods = bsObj.findAll('span', {'class':'excitingNote'})
for text in blods:
    print(text.get_text())

from urllib.request import urlopen

'''
url = 'http://pythonscraping.com/pages/page1.html'
html = urlopen(url)
print(html.read())
'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://pythonscraping.com/pages/page1.html')
#print(html.read())
bsObj = BeautifulSoup(html.read(), 'html.parser')
#print(bsObj.title)
#print(bsObj.h1)
#print(bsObj.body)
#print(bsObj.div)
print(bsObj.body.h1)

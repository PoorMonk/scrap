from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bsObj = BeautifulSoup(html, 'html.parser')
#nameList = bsObj.findAll('span', {'class':'green'})
lineList = bsObj.findAll('span', {'class':{'green', 'red'}})
#print(lineList)
#for line in lineList:
#    print(line.get_text())
namelist = bsObj.findAll(text='the prince')
#print(namelist)
allText = bsObj.findAll(id='text')
print(allText[0].get_text())

import requests, time
import urllib.request
from bs4 import BeautifulSoup

source = urllib.request.urlopen('http://coinmarketcap.com').read()
soup = BeautifulSoup(source, 'lxml')
data = []
table = soup.find('table')
table_body = soup.find('tbody')

rows = soup.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) 

for x in data:
    print(x[0:7])
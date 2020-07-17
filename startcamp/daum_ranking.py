import requests
from bs4 import BeautifulSoup

url = 'https://www.daum.net/'
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')

selects = []
for i in range(1,4):
    for j in range(1,6):
        selects.append(data.select_one(f'#wrapSearch > div.slide_favorsch > ul:nth-child({i}) > li:nth-child({j}) > a').text)

for s in selects:
    print(s)
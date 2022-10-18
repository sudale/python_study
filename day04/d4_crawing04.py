import re
from matplotlib.cbook import strip_math
import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.daum.net/economic/')
soup = BeautifulSoup(res.content, 'html.parser')

links = soup.select('a[href]')
# print(links)
for t in links:
    if re.search('https://v.\w+', t['href']):  # .  임의의 문자 1개
        print(t.get_text().strip())           # \w 숫자와 문자
        # +  1회 이상

print('----------------------------------------------')

links = soup.find_all(href=re.compile(r'https://v.\w+'))
for e in links:
    print(e.get_text().strip())

import re
import requests
from bs4 import BeautifulSoup

res = requests.get('https://m.dhlottery.co.kr/gameResult.do?method=byWin')
soup = BeautifulSoup(res.content, 'html.parser')

lotto = soup.select(
    'div.bx_lotto_winnum span')

for a in lotto:
    print(a.string, end=' ')

ballNum = soup.find_all('span', class_='ball')

for i in ballNum:
    print(i.get_text(), end=' ')

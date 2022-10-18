from bs4 import BeautifulSoup
import re
from matplotlib.pyplot import text
import requests

r = requests.get("http://api.aoikujira.com/time/get.php")
txt = r.text  # 텍스트 형식으로 데이터 추출
print(text)

bin = r.content  # 바이너리 형식으로 데이터 추출
print(bin)

################################################

html = """
    <ul>
        <li><a href="hoge.html">hoge</li>
        <li><a href="https://example.com/fuga">fuga*</li>
        <li><a href="https://example.com/foo">foo*</li>
        <li><a href="shttps://example.com/foobbb">foobbb*</li>
        <li><a href="http://example.com/aaa">aaa*</li>
    </ul>
"""

soup = BeautifulSoup(html, 'html.parser')

lis = soup.find_all(href=re.compile(r'https://'))  # https 있는 모든거 출력
print(lis)

lis1 = soup.find_all(href=re.compile(r'^https://'))  # https 시작하는
print(lis1)

for e in lis1:
    # print(e) <a href="https://example.com/fuga">fuga*</a>
    print(e.attrs['href'])

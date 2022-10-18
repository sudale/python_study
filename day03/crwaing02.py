from bs4 import BeautifulSoup
import urllib.request as req


url = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

res = req.urlopen(url)
print(res)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)

# 기상청 육상 중기예보 : title 만 출력
title = soup.channel.title.string
print(title)
title1 = soup.find('title').string
print(title1)

wf = soup.find('wf').string
print(wf)

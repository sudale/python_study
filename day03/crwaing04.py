from bs4 import BeautifulSoup
import urllib.request as req

url = "https://finance.naver.com/marketindex/"

res = req.urlopen(url)
soup = BeautifulSoup(res, 'html.parser')
# print(soup)
# #exchangeList > li > a.head > div
txt = soup.select_one('#exchangeList > li > a.head > div')
print(txt)

print("value :", soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.value').string)

txt1 = soup.select_one('div.head_info')
print('>>> ', txt1)
print(txt1.select('span')[0].string)
print(txt1.select('span')[1].string)
print(txt1.select('span')[2].string)
print(txt1.select('span')[3].string)

txt2 = txt.select('span')  # txt2 : 리스트형
print(txt2)

for sp in txt2:
    print(sp.string)

# 가격
price = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.value').string
print(price)

# 상승 하락
updown = soup.select_one(
    '#exchangeList > li.on > a.head.usd > div > span.blind').string
print(updown)

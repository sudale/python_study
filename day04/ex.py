from bs4 import BeautifulSoup
import requests

req = requests.get("https://comic.naver.com/webtoon/weekday?order=ViewCount")
html = req.text

soup = BeautifulSoup(html, 'html.parser')

webtoon_ranking_list = soup.select(
    '#content > div.list_area.daily_all > div.col.col_selected > div > ul > li a.title')

for i in range(len(webtoon_ranking_list)):
    print((i+1), '위 :', webtoon_ranking_list[i].get_text().strip())

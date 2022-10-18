from bs4 import BeautifulSoup
import requests

req = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.naver")
html = req.text

soup = BeautifulSoup(html, 'html.parser')

movie_ranking_list = soup.select('div.tit3 a')

for a in movie_ranking_list:
    print(a.string)

print('-------------------------------------')

movie_ranking_list = soup.find_all('div', class_="tit3")
print(type(movie_ranking_list))

for i in movie_ranking_list:
    print(i.get_text().strip())

print('----------------------------------')  # 순위
for i in range(len(movie_ranking_list)):
    print((i+1), '위 :', movie_ranking_list[i].get_text().strip())

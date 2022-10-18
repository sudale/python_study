
from unittest import result
from bs4 import BeautifulSoup
import requests
import pandas as pd

header = {'User-Agent': 'Mozilla/5.0'}
req = requests.get(
    'https://www.melon.com/chart/week/index.htm', headers=header)
soup = BeautifulSoup(req.text, 'html.parser')

tbody = soup.select_one('#frm > div > table > tbody')
# print(tbody)
trs = tbody.select('tr')

datas = []
for i in trs:
    rank = i.select_one('div > span').get_text()
    song = i.select_one('div > span > a').get_text()
    name = i.select_one('div.ellipsis.rank02 > a').get_text()
    album = i.select_one(
        'td:nth-child(7) > div > div > div > a').get_text()
    datas.append([rank, song, name, album])

# print(datas)

melon_df = pd.DataFrame(datas, columns=('순위', '곡명', '가수명', '앨범'))
# print(melon_df)
melon_df.to_csv('melon.csv', encoding='utf-8', mode='w', index=False)

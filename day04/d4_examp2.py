from openpyxl import Workbook
import requests
from bs4 import BeautifulSoup


res = requests.get('https://finance.naver.com/')
soup = BeautifulSoup(res.content, 'html.parser')

# list = soup.select(
#     '#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > th > a')
# # print(list)
# stock = soup.select(
#     '#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > td:nth-child(2)')
# # print(stock)
# blind = soup.select(
#     '#container > div.aside > div > div.aside_area.aside_popular > table > tbody > tr > td > span')
# # print(blind)

# print(len(list))
# print(len(stock))
# print(len(blind))
# for i in range(len(list)):
#     print('[', list[i].get_text().strip(),
#           stock[i].get_text().strip(),
#           blind[i].get_text().strip(), ']')

tbody = soup.select_one(
    '#container > div.aside > div > div.aside_area.aside_popular > table > tbody')

trs = tbody.select('tr')

datas = []
for i in trs:
    name = i.select_one("th > a").get_text()
    curr_price = i.select_one('td').get_text()
    ch_direction = i.select_one('td > img')['alt']
    ch_updown = i.select_one('td > span').get_text().strip()
    datas.append([name, curr_price, ch_direction, ch_updown])

print(datas)

write_wb = Workbook()
write_ws = write_wb.create_sheet('결과')
for data in datas:
    write_ws.append(data)

write_wb.save(r'financeWork.xlsx')

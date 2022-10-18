from unittest import result
import pymysql
import requests
from bs4 import BeautifulSoup

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser,
                       passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True)

# 부산의 날씨
select_data = "select * from forecast where city='부산' order by tmef desc"
cur = conn.cursor()
cur.execute(select_data)
result = cur.fetchall()

datas = []
for row in result:
    datas.append([row[2], row[4], row[5]])
# print(datas)

# 부산의 날짜 최저기온, 최고기온
select_data2 = "select max(tmax), min(tmn) from forecast where city='부산'"

cur.execute(select_data2)
result2 = cur.fetchone()
print(result2)
print("최고 :" + result2[0])
print("최저 :" + result2[1])

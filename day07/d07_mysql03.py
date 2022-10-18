from symbol import yield_arg
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser,
                       passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True)

# 부산의 날씨
select_data = "select * from forecast where city='부산'"

font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()

mpl.rc('font', family=font_name)

cur = conn.cursor()
cur.execute(select_data)

result = cur.fetchall()

high = []
low = []
xdata = []
whState = []

for row in result:
    high.append(float(row[5]))  # 최고기온
    low.append(float(row[4]))  # 최저기온
    whState.append(row[3])  # 날씨 상태
    xdata.append(row[2].split('-')[2])  # 가로축

plt.figure(figsize=(10, 6))  # 그래프크기
plt.plot(xdata, low, label="최저기온")
plt.plot(xdata, high, label="최고기온")
plt.title(result[0][2].split('-')[1]+"월")  # 타이틀

plt.legend()
plt.show()

# wf
select_data1 = "select wf, count(*) from forecast where city='부산' group by wf"
print(select_data1)


cur.execute(select_data1)
result1 = cur.fetchall()
whData = []
whDataCount = []
for row in result1:
    whData.append(row[0])
    whDataCount.append(row[1])

# bar
plt.bar(whData, whDataCount)
plt.show()

# pie
plt.pie(whDataCount, labels=whData, autopct='%.1f%%')
plt.show()

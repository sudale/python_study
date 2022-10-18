from symbol import yield_arg
import pymysql
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import pandas as pd

dbURL = "127.0.0.1"
dbPort = 3306
dbUser = "root"
dbPass = "1234"
conn = pymysql.connect(host=dbURL, port=dbPort, user=dbUser,
                       passwd=dbPass, db='bigdb', charset='utf8', use_unicode=True, cursorclass=pymysql.cursors.DictCursor)

# 부산의 날씨
select_data = "select * from forecast where city='서울'"

font_name = mpl.font_manager.FontProperties(
    fname='c:/Windows/fonts/malgun.ttf').get_name()

mpl.rc('font', family=font_name)

cur = conn.cursor()
cur.execute(select_data)

result = cur.fetchall()

df = pd.DataFrame(result)
print(df)

plt.plot(pd.to_numeric((df['tmn'])), label='최저기온')
plt.plot(pd.to_numeric((df['tmax'])), label='최고기온')

plt.legend()
plt.show()

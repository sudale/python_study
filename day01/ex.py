# 1.
import pandas as pd


str = '20201231Thursday'
print(str[0:4])
print(str[4:8])
print(str[8:16])

print('--------------------------')
# 2.
a = ['쓰', '레', '기', '통']
a.reverse()
print(a)

print('--------------------------')
# 3.
dict = {'year': 2020, 'mm': 12, 'dd': 31, 'day': 'Thursday', 'weather': 'snow'}
print(dict.keys())
print(dict.values())

print('--------------------------')
# 5.
i = 0
while i < 5:
    i += 1
    print('*'*i)

print('--------------------------')
# 6.


def avg(*args):
    x = 0
    for i in args:
        x += i
    return x/len(args)


print(avg(5, 3, 12, 9))
print(avg(2.4, 3.2, 7.3))
print(avg(10, 5))

print('--------------------------')
# 7.
df2 = pd.DataFrame([
    [500, 450, 520, 610], [690, 700, 820, 900],
    [1100, 1030, 1200, 1380], [1500, 1650, 1700, 1850],
    [1990, 2020, 2300, 2420], [1020, 1600, 2200, 2550]
], index=['2015', '2016', '2017', '2018', '2019', '2020'],
    columns=['1분기', '2분기', '3분기', '4분기'])
df2.to_csv('c:/test/score1.csv', header='False')

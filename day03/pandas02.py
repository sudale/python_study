import pandas as pd
# name ==> 'Mark', 'Jane', 'aaa', 'rr'
# age ==> 33, 44, 55, 11
# score ==> 91.2, 88.5, 55.6, 88.9

data = {
    'name': ['Mark', 'Jane', 'aaa', 'rr'],
    'age': [33, 44, 55, 11],
    'score': [91.2, 88.5, 55.6, 88.9]
}
print(type(data))
# data 를 데이터프레임 으로 생성
df = pd.DataFrame(data)

print(df)
print(type(df))
print(df.sum())  # 합계
print(df.mean())  # 평균
print(df.age)
print(df['age'])

# year sales
# 2018 350
# 2019 400
# 2020 1050
# 2021 2000
# 2022 1000
data_dic = {
    'year': [2018, 2019, 2020, 2021, 2022],
    'sales': [350, 400, 1050, 2000, 1000]
}
# 데이터프레임으로
df2 = pd.DataFrame(data_dic)
print(df2)

#          1반   2반   3반
# 중간고사 89.2, 92.5, 90.8
# 기말고사 92.8, 89.9, 95.2

df3 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   index=['중간고사', '기말고사'],
                   columns=['1반', '2반', '3반'])
print(df3)

df4 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]],
                   columns=['1반', '2반', '3반'])
df4.index = ['중간인덱스', '기말인덱스']
print(df4)

df5 = pd.DataFrame([[89.2, 92.5, 90.8], [92.8, 89.9, 95.2]])
df5.index = ['중간인덱스', '기말인덱스']
df5.columns = ['A', 'B', 'C']
print(df5)

# df3 sum() 출력
print("###############################")
print(df3.sum())

# 1반 합계 출력
print(df3['1반'].sum())
print(df3['1반'].mean())
print(df3.mean())

# df5 를 df5.csv 내보내기
# df5.to_csv('df5.csv', header='False')

df_read = pd.read_csv('df5.csv', encoding='utf-8')
print(df_read)

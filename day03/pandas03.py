import pandas as pd

# survey.csv 읽어서 위에서 5개 출력
df = pd.read_csv('day03/survey.csv')
print(df.head())
# 평균
print(df.mean())
# 수입의 평균 (반올림해서 소수점 1자리까지 표현)
print('수입의 평균 :', df.income.mean())
print('수입의 평균 반올림 :', round(df.income.mean(), 1))

print('수입의 합계 :', df.income.sum())
# 수입중앙값
print('수입의 수입중앙값 :', df.income.median())

# describe()
print(df.describe())

print(df.income.describe())
print(df.sex.value_counts())

import csv

import re

f = open('popSeoul.csv', 'r')
reader = csv.reader(f)
# print(reader)
output = []
# for i in reader:
#     output.append(i)
# print(output)

# 숫자만 읽어와서 ,를 제거하고 float 형태로 변환하여 output 추가
# 문자는 그대로 output 추가
# for i in reader:
#     tmp = []
#     for j in i:
#         if re.search('\d', j):
#             tmp.append(float(re.sub(',', '', j)))
#         else:
#             tmp.append(j)
#     output.append(tmp)
# print(output[:3])

for i in reader:
    tmp = []
    for j in i:
        try:
            if re.search('\d', j):
                tmp.append(float(re.sub(',', '', j)))
            else:
                tmp.append(j)
        except:
            pass
    output.append(tmp)
print(output[:3])

# '구', '한국인', '외국인', '외국인 비율(%) = 외국인/(한국인+외국인)*100'
print('-----외국인-----')
ko_fo = [['구', '한국인', '외국인', '외국인 비율(%)']]
for i in output:
    try:
        foreign = round(i[2]/(i[1]+i[2])*100, 1)
        if foreign > 5:
            ko_fo.append([i[0], i[1], i[2], foreign])
    except:
        pass
print(ko_fo)
print(len(ko_fo))


# animal 리스트에서 새가 저장되어 있는 위치 저장하는 리스트
from yaml import add_multi_constructor


bird_pos = []
animals = ['새', '코끼리', '강아지', '새', '강아지', '새']

# for i in range(len(animals)):
#     # print(i)
#     if(animals[i] == '새'):
#         bird_pos.append(i)

for i, animal in enumerate(animals):
    if(animal == '새'):
        bird_pos.append(i)

print('새 위치 :', bird_pos)

# myList 에서 짝수만 출력
myList = [3, 5, 4, 9, 2, 8, 2, 1]
new_List = []

for i in myList:
    if i % 2 == 0:
        new_List.append(i)

print(new_List)

# 리스트 함축 : for문과 if 조건식을 함축적으로 결합한 형식
# [i for i in 리스트명 if 조건식]
new_list2 = [i for i in myList if (i % 2) == 0]

print(new_list2)

# 19세 이상인 사람만 추출하여 리스트 adult에 저장
people = [31, 53, 19, 15, 18, 21, 13]
adult = [i for i in people if i >= 19]

print(adult)

# 항목이 2개인것문 추출하여 twolist에 추가
lists = [[1, 2], [3, 4, 5, ], [6, 7]]
twolist = [i for i in lists if len(i) == 2]

print(twolist)

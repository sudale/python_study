import codecs
import re
from tkinter.font import names

from numpy import character

f = codecs.open('friends101.txt', encoding='utf-8')
script101 = f.read()

print(script101[:100])
lines = re.findall(r'Monica:.', script101)
print(lines[:3])
print(type(lines))
# script101 에서 All:
All = re.findall(r'All:.+', script101)
print(All)
# All 에서 마지막 출력
print(All[-1])
print(len(All))
print('--------------------------')
char = re.compile(r'[A-Z][a-z]+:')
print(re.findall(char, script101))
names = re.findall(char, script101)
print(len(names))
print('-----------------')
print(set(re.findall(char, script101)))
print(set(names))
print(len(set(names)))

print('-------------------------')
setType = set(re.findall(char, script101))
print(type(setType))

# 등장인물 이름이 7자 이상인 사람 출력
for i in setType:
    if len(i) > 7:
        print("== : ", i)

character = list(setType)  # list로
print(type(character))
print(character)
# character에서 : 제거해서 출력
character_list = []
for i in character:
    character_list += [i[:-1]]
print('character_list :', character_list)

character_list2 = []
for i in character:
    character_list2 = re.sub(':', '', i)
    print(character_list2, end=' ')
print(character_list2)

a = '제 이메일 주소는 greate@naver.com'
a += '오늘은 today@naver.com 내일은 apple@gamil.com life@abc.co.kr 라는 메일을 사용합니다.'
print(a)

# ['greate@naver.com','today@naver.com','apple@gmail.com','life@abc.co.kr']
# 패턴 : 영문자 @ 영문자 .
a1 = re.findall(r'[a-z]+@[a-z.]+', a)
print(a1)

words = ['apple', 'cat', 'brave', 'drama', 'asise', 'blow', 'coat', 'above']
# ['apple','at','ave','ama','asise','at','above']
# 패턴 : a영문자
words_list = []
for i in words:
    words_list += re.findall(r'a.+', i)
print(words_list)
print('-------------------------')

for i in words:
    m = re.search(r'a[a-z]+', i)  # search는 찾고자 하는 단어가 중간에 있어도 찾음
    if m:
        print(m.group())
print('-------------------------')

for i in words:
    # m = re.match(r'a[a-z]+', i) # search는 찾고자 하는 단어가 첫음에 있어야 함
    m = re.match(r'a\D+', i)  # \d(숫자) \D(숫자가 아닌)
    if m:
        print(m.group())

exam1 = '저는 91년에 태어났습니다. 97년에는 IMF가 있었습니다. 지금은 2022년입니다.'
print(re.findall(r'\d+년', exam1))

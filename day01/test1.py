print('Hello')

a = 0
print(a)
print(type(a))
b = 'Hello World'
print(b)
print(type(b))
c = "'안녕하세요'"
print(c)
d = "\'안녕하세요\'"
print(d)
print(b+d)
print(2*3)
print('2'*3)
print(c*3)

# b[1] = 'C' 오류발생 문자는 변경불가
print('-------------------------------------')
print(b)
print(b[0])
print(b[-1])
print(b[-2])

e = '반갑습니다'
print(e)
print(e[0:2])
print(e[1:3])
print(e[:])
print(e[0:5:2])
print(e.find('반'))
print(e.find('니'))
print(e.find('안'))  # 없으면 -1 리턴

print(e.index('반'))
print(e.index('니'))
# print(e.index('안'))  # 없으면 오류발생

bb = ','
print(bb.join('ABCD'))
print(bb)
print(b.upper())
print(b.lower())
print(b)

# 공백제거
dd = '           py           '
print(dd.lstrip())  # 왼쪽 제거
print(dd.rstrip())  # 오른쪽 제거
print(dd.strip())  # 양쪽 제거

aa = 'Now is aa bb cc'
print(aa.split())  # [] 대괄호로 나눠짐

# 리스트 (list) []
l = list()
print(l, type(l))
lst = [1, 2, 3]
print(lst, type(lst))
# 리스트 L2 1부터 11까지로 이루어진 리스트 L2 생성
l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# L2 유형확인
print(l2, type(l2))
# L2 첫번째 값  출력
print(l2[0])
# L2 길이
print(len(l2))
print(l2[-1])
# L2의 마지막 값 출력
print(l2[len(l2)-1])  # L2 에서 마지막 원소(L2의 길이 -1)
# L2의 첫번째 값을 99로 수정
l2[0] = 99
print(l2)
l2[1] = [1, 2, 3]
print(l2)  # 리스트안에 리스트가 들어갈수 있음
print(len(l2))
l2[2] = '문자'
print(l2)

# 마지막에 추가 append
l2.append(999)
print(l2)

# 제거 remove
l2.remove(5)
print(l2)

# 1,2,3으로 이루어진 a1 리스트 생성
a1 = [1, 2, 3]
# 'life', 'is', 'too', 'short' 이루어진 b1 리스트 생성
b1 = ['life', 'is', 'too', 'short']
# 1,2,'life','is' 이루어진 c1 리스트 생성
c1 = [1, 2, 'life', 'is']
# 1,2, (3,4), ('life','is) d1 리스트 생성
d1 = [1, 2, [3, 4], ['life', 'is']]

# d1의 첫번째 값 출력
print(d1[0])
print(d1[3])
print(d1[3][-1])
print(d1[0:3])

# insert 위치정하여 추가
d1.insert(2, 'aa')
d1.append('dd')
print(d1)
print(len(d1))

# pop 마지막 요소를 돌려줌
d1.pop()
print(d1)

a2 = [2, 1, 0, 2, 3, 2, 4, 2]
print(a2.count(2))

######################################

# 튜플(tuple) - 수정 불가능 ()
t = tuple()
print(t, type(t))
t1 = (1, 2, 3)
print(t1, type(t1))
print(t1[0], t1[0:2])
print(t1+t1)
# t[0] = 5  수정 불가능
t4 = (1, 2, (3, 4,), ('life', 'is'))
print(t4)

# dict (자바에서 Map과 같음) {}
d = dict()
print(d, type(d))
d1 = {
    'a': 1,
    'b': 2,
    'c': 3
}
print(d1, type(d1))
print(d1['a'])  # key 값을 넣으면 value 값이 호출된다
d1['c'] = 33
print(d1)
print("keys() : ", d1.keys())  # key 값만 알려줌
print("values() : ", d1.values())  # value 값만 알려줌
print("items : ", d1.items())

##################################

print("type keys() : ", type(d1.keys()))
print("type values() : ", type(d1.values()))
print("type items() : ", type(d1.items()))
print('#####################################')
print("type list", type(list(d1.keys())))

# 1. name은 Hong, phone은 01011112222, birth는 0814로 이루어진 dict 생성
dict = {
    'name': 'Hong',
    'phone': '01011112222',
    'birth': '0814'
}
print(dict)
# 2. dict 키값이 1이고 value가 'a'를 추가
dict[1] = 'a'
print(dict)
# 3. dict 키값이 pet이고 value가 'dog'를 추가
dict['pet'] = 'dog'
print(dict)
# 4. key가 pet은 value  값 출력
print(dict['pet'])
# dict에서 key값만 출력
print(dict.keys())
print("keys() : ", dict.keys())
# 리스트 형태로 key 값만 출력
lst = list(dict.keys())
print(lst)
print(list(dict.keys()))
del dict[1]
print('dict:', dict)
dict.clear()  # 키값, 밸류값 삭제
print(dict)

# set key와 value로 이루어져있지 않고 key로 이루어져 있음
s1 = {1, 2, 3, 4, 4, 4, 4}
print(s1, type(s1))
s2 = set([1, 2, 3, 4, 5])
print(s2, type(s2))
print(s1 & s2)
print(s1 | s2)
print(s1-s2)
print(s2-s1)
print(s2.difference(s1))
# 리스트, 튜플, 딕셔너리, set

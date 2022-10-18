import re


text = "<title>지금은 문자열 연습입니다<title>"
# 1. 0~7 사이 추출
print(text[0:7])
# 2. 문 있으면 위치값 출력
print(text.find('문'))
# 3. 파 있으면 위치값 출력 없으면 -1 출력
print(text.find('파'))
# 4. 파 있으면 위치값 출력 없으면 오류
# print(text.index('파'))

text1 = "     <title>지금은 문자열 연습입니다<title>     "
text2 = ";"
# 1. text1 공백제거하고 text2 연결
print(text1.strip()+text2)
# 2. text1 왼쪽공백제거하고 text2 연결
print(text1.lstrip())
# 3. text1 오른쪽공백제거하고 text2 연결
print(text1.rstrip())
# 4. text1 <title>을 <div>로 바꾸기
print(text1.replace("<title>", "<div>"))

text3 = ('111<head>안녕하세요</head>22')
body = re.search('<head.*/head>', text3)
print(body)
body = body.group()
print(body)

print("-----------------------------")
text4 = ('<head>안녕하세요...<title>지금은 문자열 연습</title></head>')
# search 사용 : <title>지금은 문자열 연습</title>
body = re.search('<title.*/title>', text4)
print(body)
body = body.group()
print(body)
body = re.sub('<.+?>', ' ', text4)
print(body)

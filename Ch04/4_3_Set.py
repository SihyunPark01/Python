"""
날짜 : 2021/08/10
이름 : 박시현
내용 : 파이썬 자료구조 Set 실습하기 교재 p92
"""


#Set 중복값안됨, 순서의미없음
set1 = {1, 2, 3, 4, 5, 3, 2}
print(type(set1))
print(set1)

set2 = set('Hello World')
print(type(set2))
print(set2)

#리스트 변환 후 출력
list1 = list(set1)
print(list1)
print(list1[0])
print(list1[3])


list2 = list(set2)
print(list2)
print(list2[0])
print(list2[3])
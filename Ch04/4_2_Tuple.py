"""
날짜 : 2021/08/10
이름 : 박시현
내용 : 파이썬 자료구조 Tuple 실습하기 교재 p92
"""



#Tuple(고정 리스트 : 추가, 삭제, 수정이 안됨) list는 대괄호, tuple은 소괄호
tuple1 = (1, 2, 3, 4, 5)
print('tuple1 type: ', type(tuple1))
print('tuple1[0]: ', tuple1[0])
print('tuple1[2]: ', tuple1[2])
print('tuple1[3]: ', tuple1[3])

tuple2 = ('서울','대전','대구','부산','광주')
print('tuple2 type: ', type(tuple1))
print('tuple2[0]: ', tuple2[0])
print('tuple2[2]: ', tuple2[2])
print('tuple2[3]: ', tuple2[3])

# 튜플 수정, 삭제 -> 불가능
tuple3 = 1, 2, 3, 4, 5      #괄호 생략 가능
tuple3[0] = 7
print(tuple3)



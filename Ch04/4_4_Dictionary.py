"""
날짜 : 2021/08/10
이름 : 박시현
내용 : 파이썬 자료구조 Dictionary 실습하기 교재 p92
"""


# Dictionary(key-Value) json이랑 비슷함!!! key값을 출력시키면 value값이 출력됨
dic1 = {
    'A' : 'Apple',
    'B' : 'Banana',
    'C' : 'Cherry'
}

print('dic1 type :', type(dic1))
print('dic1 :', dic1)
print("dic1['A'] :", dic1['A'])
print("dic1['B'] :", dic1['B'])
print("dic1['C'] :", dic1['C'])

dic2 = {
    1: '서울',
    2: '대전',
    3: '대구',
    4: '부산',
    5: '광주'

}

print('dic2[1] :', dic2[1])
print('dic2[4] :', dic2[4])


dic3 = {
    101: [1, 2, 3, 4, 5], #list
    102: (6, 7, 8, 9, 10), #tuple
    103: {'한국','미국','일본','중국'}, #집합
    104: {'p1': '김유신', 'p2': '김춘추', 'p3': '장보고'}  #dictionary
}

print('dic3[101][2] :', dic3[101][2])
print('dic3[102][1] :', dic3[102][1])
print('list(dic3[103])[0] :', list(dic3[103])[0])
print(dic3[104]['p2'])

# 응용
dics = [dic1, dic2, dic3]



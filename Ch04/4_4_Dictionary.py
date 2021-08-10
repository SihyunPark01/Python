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

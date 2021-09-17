"""
날짜 : 2021/09/03
이름 : 박시현
내용 : 코딩테스트 - 위에서 아래로
"""

n = int(input())

array = []

for i in range(n):
    num = int(input())
    array.append(num)

array.sort(reverse=True)

for num in array:
    print(num, end=' ')
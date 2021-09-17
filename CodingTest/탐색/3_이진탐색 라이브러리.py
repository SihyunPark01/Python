"""
날짜 : 2021/09/17
이름 : 박시현
내용 : 코딩테스트 - 이진탐색 라이브러리 함수
"""
# pos는 초기값, 인덱스번호
# 존재하지 않는 수는 그 수의 위치값이 나옴.

from bisect import bisect_left

dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 : '))

pos = bisect_left(dataset, value)
print('pos :', pos)

def BinarySearch(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target: #존재하지 않는 수다
        return i
    else:
        return -1


value = int(input('검색할 숫자 : '))
pos = BinarySearch(dataset, value)

if pos == -1:
    print('찾으시려는 숫자가 없습니다.')
else:
    print('%d는 %d번째에 있습니다.' % (value, pos))


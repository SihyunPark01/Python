"""
날짜 : 2021/09/17
이름 : 박시현
내용 : 코딩테스트 - 부품 찾기
"""

from bisect import  bisect_left

def BinarySearch(dataset, target):
    i = bisect_left(dataset, target)
    if dataset[i] == target:
        return i
    else:
        return -1

# N(부품 개수) 입력
n = int(input())

# 가게에 있는 전체 부품 번호를 공백 구분해서 입력
dataset = list(map(int, input().split()))
# 이진탐색 전 정렬 필수 수행
dataset.sort()

# M(손님이 요청한 부품 개수) 입력
m = int(input())

# 손님이 요청한 부품번호 공백 구분해서 입력
requests = list(map(int, input().split()))
# 이미 정렬이 되어있기 때문에 다시 정렬 할 필요가 없음

# 손님이 요청한 부품번호를 하나씩 확인
for num in requests:
    # 해당부품이 존재하는지 확인
    result = BinarySearch(dataset, num)
    if result == -1:
        print('no', end=' ') #출력 시 세로가 아닌 공백과 함께 가로로 출력되게끔 해주는 작업이 end=' '
    else:
        print('yes', end=' ')

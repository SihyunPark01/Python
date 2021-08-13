"""
    날짜 : 2021/08/13
    이름 : 박시현
    내용 :  코딩테스트 - 큰수의 법칙


"""

n, m, k = map(int, input().split())   #map : 일괄처리

data = list(map(int, input().split()))

#큰수부터 정렬
data.sort(reverse=True)

# 가장 큰 수, 두번째로 큰 수
first = data[0]
second = data[1]


result = 0
repeat = k

for i in range(m): #더하기를 m번 돌린다

    if repeat > 0:
        result += first
        repeat -= 1
    else:
        result += second # 두번째 큰수를 1번 더한다.
        repeat = k

print(result)









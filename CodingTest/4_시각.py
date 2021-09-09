"""
    날짜 : 2021/08/20
    이름 : 박시현
    내용 :  코딩테스트 - 시각
"""

n = int(input())

count = 0

for i in range(n + 1):
    for j in range (60):
        for k in range(60):

        # if('3'이 포함된 시간이면):

            time = str(i) + str(j) + str(k)

            if '3' in time:
                count += 1


print(count)

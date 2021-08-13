



n, m = map(int, input().split())
mins = [] #min값 저장용 리스트
result = 0


for i in range(n):
    # 행 데이터 입력하기
    data = list(map(int, input().split()))
#data2 = list(map(int, input().split))
#data3 = list(map(int, input().split))

    # 데이터 오름차순 정렬
    data.sort()

    # 최소값 구하기
    min = data[0]

    # 각 행의 최소값 저장하기
    mins.append(min)


# mins에서 최대값 구하기
result = max(mins)

print(result)
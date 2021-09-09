"""
    날짜 : 2021/08/20
    이름 : 박시현
    내용 :  코딩테스트 - 상하좌우
"""

#n값 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

for plan in plans:

    if plan == 'L':
        if y == 1:
            continue
        else:
            y -= 1

    if plan == 'R':
        if y == 5:
            continue
        else:
            y += 1
    if plan == 'U':
        if x == 1:
            continue
        else:
            x -= 1
    if plan == 'D':
        if x == 5:
            continue
        else:
            x += 1

print(x, y)

"""
n = int(input())
x, y = 1, 1
plans = input().split()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나면 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동하기
    x, y = nx, ny
print(x, y)
"""




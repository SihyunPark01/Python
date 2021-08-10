"""
날짜 : 2021/08/10
이름 : 박시현
내용 : 파이썬 while문 실습하기 교재 p64
"""

#for
for i in range(5): #range함수를 써서 반복횟수를 적어준다
    print('{}회 반복'.format(i))

for i in range(10, 15):     #10,11,12,13,14
    print('%d회 반복' % i)

for i in range(5, 0, -1):   #5,4,3,2,1
    print(i,'회 반복')


#1부터 10까지 합
total = 0

for k in range(11): #10까지 돌리려면 11을 적어줘야 함
    total += k

print('1부터 10까지 합 :', total)


#1부터 10까지 짝수합
eSum = 0

for k in range(11):
    if k % 2 == 0:
        eSum += k

print('1부터 10까지 짝수합 :', eSum)


#중첩 for문 ----총 15번 돌겠네 1라운드에 5번, 2라운드에 5번 이런식으로...
for a in range(3):
    print('a :', a)

    for b in range(5):
        print('b :', b)


#구구단
for x in range(2, 10):

    print('%d단' % x)
    for y in range(1, 10):
        z = x * y
        print('%d X %d = %d' % (x, y, z))



#별삼각형 역삼각형 3가지 방법
for a in range(11):
    for b1 in range(a): #위에 range(11)그대로 두고 여기 range에 (10-a) 해도 됨
        print('☆', end='')

    print()

for a1 in range(10, 0, -1):

    for b1 in range(a1): #위에 range(11)그대로 두고 여기 range에 (10-a) 해도 됨
        print('☆', end='')

    print()

for a2 in range(11):
    for b2 in range(10-a2):
        print('☆', end='.')
    print()

for i in range(11):
    print('★' * i)
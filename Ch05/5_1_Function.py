"""
    날짜: 2021/08/11
    이름: 박시현
    내용: 파이썬 함수 실습하기 교재 p114
"""

# 함수 정의 (일련의 로직을 재활용하기 위해 모듈화한 로직단위)
def f(x):
    y = 2 * x + 3
    return y


# 함수 호출
y1 = f(1)   #1은 인자값(argument)
y2 = f(2)
y3 = f(3)

print('y1 :', y1)
print('y2 :', y2)
print('y3 :', y3)

# 타입1 - 매개변수 0, 리턴값 0
def type1(x, y):
    z = x + y
    return z
r1 = type1(1, 2)
r2 = type1(2, 3)
print('r1: ', r1)
print('r2: ', r2)


# 타입2 - 매개변수 0, 리턴값 X ---- 보통 for문에서 사용됨, items가 list가 된다고???
def type2(items):
    tot = 0

    for item in items:
        tot += item

    print('items의 합 : ', tot)

type2([1, 2, 3, 4, 5])
type2((1, 3, 5, 7, 9))      #튜플 타입


# 타입3 - 매개변수 X, 리턴값 0
def type3():

    total = 0
    for k in range(11):
        total += k

    return total

r3 = type3()
print('r3: ', r3)



# 타입4 - 매개변수 X, 리턴값 X
def type4():
    print('type4() :', type3())

type4()   # 왜 이걸 쳐야 출력이 되는거지???


# 연습문제

def gugudan(n):
    print('%d단' % n)
    for i in range(1,10):
        y = n * i
        print('%d X %d = %d' % (n, i, y))

gugudan(3)

gugudan(7)










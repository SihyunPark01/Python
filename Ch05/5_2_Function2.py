"""
    날짜: 2021/08/11
    이름: 박시현
    내용: 파이썬 함수고급 실습하기 교재 p129
"""



# 디폴트 매개변수
def hello(name='홍길동', age=21): #매개변수에 디폴트값을 선언해놓으면 밑의 함수가 모두 출력됨.
    print('이름 :', name)
    print('나이 :', age)

hello()
hello('김유신')
hello('김춘추', 25)

# 가변 매개변수
def total(*scores): #*을 선언하면 변수의 개수가 상관없이 선언가능함, 자바에서는 scores... 으로 선언했었지.
    tot = 0

    for score in scores:
        tot += score

    return tot

r1 = total(1, 2, 3)
r2 = total(1, 2, 3, 4, 5)
r3 = total(1, 2, 3, 4, 5, 6, 7)

print('r1 :', r1)
print('r2 :', r2)
print('r3 :', r3)

# 하나 이상의 리턴값 ----- 일반적으로는 1개의 함수에 1개의 리턴값을 가지지만, 파이썬에서는 하나이상의 리턴값을 출력할 수 있음
def plus_multi(num1, num2):
    y1 = num1 + num2
    y2 = num1 * num2
    return y1, y2 #리턴값이 2개지? 이게 가능한게 파이썬이드아하하아아아 -----자바는 객체를 리턴시키면 되겠지뭐~

rs1, rs2 = plus_multi(2, 3)
print('rs1: ', rs1)
print('rs2: ', rs2)

# 변수에 저장하는 함수 와우 이게 가능하구나 파이썬너란놈!!!
def plus(x, y):
    return x + y

def minus(x, y):
    return x - y

var1 = plus     #변수 var1에 plus함수를 담음
var2 = minus

res1 = var1(1, 2)
res2 = var2(2, 3)

print('res1 :', res1)
print('res2 :', res2)

# 함수 리스트
funs = [plus, minus]
res3 = funs[0](3, 4) #[]리스트 구조에 함수를 실행시키는 것이구나
res4 = funs[1](4, 5)

print('res3 :', res3)
print('res4 :', res4)








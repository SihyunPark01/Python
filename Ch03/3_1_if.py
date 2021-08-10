"""
날짜 : 2021/08/10
이름 : 박시현
내용 : 파이썬 if문 실습하기 교재 p68
"""

#파이썬에서는 switch조건문 없대~!

#if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:                             #거짓이면 건너뜀
    print('num1은 num2보다 크다')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고, num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
    if num2 > 1:
        print('num1은 0보다 크고, 그리고 num2는 1보다 크다.')



#if~else
num3, num4 = 3, 4

if num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num3은 num4보다 작다.')


#if~elif~else
if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num3보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')

#연습문제
score = int(input('점수 입력: '))

print('입력 점수: ', score)

if score >= 90 and score <= 100:
    #점수가 90~100
    print('A입니다.')
elif 80 <= score < 90: #이렇게 써도 가능함 파이썬 스따일~!
    print('B입니다.')
elif score >= 70 and score <80:
    print('C입니다.')
elif score >= 60 and score < 70:
    print('D입니다.')
else:
    print('F입니다.') #조건에 맞지 않으면 건너뜀!!!!
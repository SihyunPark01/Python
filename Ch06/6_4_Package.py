"""
    날짜: 2021/08/12
    이름: 박시현
    내용: 파이썬 패키지 모듈 실습하기 교재 p175
"""


#__init__.py 파일이 있다는건 sub2가 파이썬 패키지 폴더임.

#1번형태
import Ch06.sub2.calc as c
#2번형태
from Ch06.sub2.calc import *

print('프로그램 시작1')

if __name__ == '__main__': #프로그램 시작점을 알림, 자바에서 메인메소드랑 같은놈
    print('프로그램 시작2')
    #1번형태
    r1 = plus(1, 2)
    r2 = minus(2, 3)
    #2번형태
    r3 = c.multi(3, 4)
    r4 = c.div(4, 2)

    print('r1 :', r1)
    print('r2 :', r2)
    print('r3 :', r3)
    print('r4 :', r4)


#7장은 교재예제로 풀어볼 것



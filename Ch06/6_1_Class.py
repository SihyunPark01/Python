"""
    날짜: 2021/08/11
    이름: 박시현
    내용: 파이썬 객체지향 프로그래밍 실습하기 교재 p148
"""


# 클래스 따로 빼고 여기 모듈 선언
from Ch06.sub1.Car import Car
from Ch06.sub1.Account import Account

# 객체 생성 : Car라는 클래스로 bmw라는 객체를 생성
bmw = Car('520d', '흰색', 5000) # new키워드도 안써도 됨
# 기능 구현
bmw.speedUp()
bmw.speedDown()
bmw.show()

bentz = Car('벤츠', '검정색', 5000)
bentz.speedUp()
bentz.speedDown()
bentz.show()

kb = Account('국민은행','101-12-1111', '김유신', 10000)
kb.deposit(40000)
kb.withdraw(5000)
kb.show()

wr = Account('우리은행', '101-11-1010', '김춘추', 30000)
wr.deposit(10000)
wr.withdraw(20000)
wr.show()


# 사실 파이썬에서는 class를 잘 쓰진 않는대... 그리고 private, public 같은 캡슐화 없대..

# 파이썬으로는 데이터 분석을 많이 하게 된대...







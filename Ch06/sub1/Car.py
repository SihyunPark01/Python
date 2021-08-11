


# sub1은 패키지, Car은 모듈(클래스)파일

# 자동차 클래스 정의
class Car:

    def __init__(self, model, color, price):   # 생성자
        # 속성 (정보) (멤버변수 선언)
        self.model = model  #자바에서는 this, 파이썬에서는 self
        self.color = color
        self.price = price

    # 기능 (행위)
    def speedUp(self):
        print('%s speed Up...'% self.model)

    def speedDown(self):
        print('%s speed Down...' % self.model)

    def show(self):
        print('차량명 :', self.model)
        print('차량색 :', self.color)
        print('차량가격 :', self.price)
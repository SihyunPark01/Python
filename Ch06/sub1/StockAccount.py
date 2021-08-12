from Ch06.sub1.Account import Account #이렇게 출처 직접 밝혀줘야 함

class StockAccount(Account): #오 이게 상속형태군


    def __init__(self, bank, id, name, balance, stock, amount, price):
        super().__init__(bank, id, name, balance)   #자바에서도 super로 객체 생성먼저 해주고 시작하듯이 파이썬도 이렇게 super생성해주기~~~!
        self.stock = stock
        self.amount = amount
        self.price = price


    def sell(self, amount, price):
        self._balance += amount * price     #_이게 자바에서 protected와 같은 의미
        self.amount -= amount

    def buy(self, amount, price):
        self._balance -= amount * price
        self.amount += amount

    def show(self):
        print('---------------------')
        print('은행명 :', self._bank)
        print('계좌번호 :', self._id)
        print('입금주 :', self._name)
        print('현재잔액 :', self._balance)
        print('주식종목 :', self.stock)
        print('주식수량 :', self.amount)
        print('주식가격 :', self.price)



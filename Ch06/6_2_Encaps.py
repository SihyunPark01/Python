"""
    날짜: 2021/08/12
    이름: 박시현
    내용: 파이썬 캡슐화 실습하기 교재 p161
"""

from Ch06.sub1.Account import Account

num1 = 1                #num1, var1라는 변수들은 stack에 저장 / heep메모리에 Account라는 함수와 인자값들을 저장 / 그래서 stack에서는 heep에 저장된 함수의 주소값을 가지고 오는 것.
var1 = True


kb = Account('국민은행', '101-101-1001', '김유신', 10000)

kb.deposit(40000)       #여기서 kb는 객체(참조변수) / 참조라는건 메모리주소변수 / stack
kb.withdraw(5000)

#캡슐화(정보은닉)을 적용해서 취약코드 예방
# kb.__balance -= 1
# kb.__balance -= 1 # 이런게 취약한 코드아니냐 withdraw를 안쓰고도 돈을 뺄수 있으니..그래서 캡슐화가 필요해


kb.show()


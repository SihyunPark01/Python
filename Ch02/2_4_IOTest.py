"""
날짜 : 2021/08/09
이름 : 박시현
내용 : 파이썬 표준입출력 실습하기 교재 p42
"""


# 파이썬 표준 입력장치
num = input('숫자 입력 : ')  # Scanner sc = new Scanner(System.in);과 같음

# 파이썬 표준 출력장치
print('num :', num)
print('num type :', type(num)) #string타입이라 연산이 안되네

# 문자열을 숫자로 변환(캐스팅)
num = int(num)
num += 1
print('num : ', num)

# 출력 옵션
print('Hello', end='~') # 한줄로
print('Busan')

print('010', '1234', '5678', sep='-') # 구분자

# 서식문자 출력
print('%d년 %d월 %d일 %s요일' % (2021, 8, 9, '월'))
print('%s요일' % '월')

# 포맷문자열 출력
print('이름 : {}\n나이 : {}\n주소 : {}\n'.format('홍길동',21,'부산광역시')) # , : 한줄에 다 나열, \n : 각각 한줄에











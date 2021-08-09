# p43 (1) 문자형 숫자 입력
num = input("숫자 입력 : ")
print('num type : ', type(num)) # <class 'str'>
print('num = ', num)
print('num = ', num*2) # 문자열에서 곱하기는 반복이랬지!!!!!

# (2) 문자형 숫자를 정수형으로 변환
num1 = int(input("숫자 입력 : ")) # str -> int
print('num1 = ', num1*2)

# (3) 문자형 숫자를 실수형으로 변환 결과값이 .0으로 도출된다는 뜻
num2 = float(input("숫자 입력 : ")) #str -> float
result = num1 + num2
print('result = ', result)

# p45 (1) value인수
print("value =", 10 + 20 + 30 + 40 + 50 )

# (2) sep인수
print("010", "1234", "5678", sep="-")

# (3) end인수
print("value=", 10, end = ", ")
print("value=", 20)

# p46 (4) format() 함수 인수 : format(value, "format")
print("원주율 =", format(3.14159, "8.3f"))  #8개자리수에서 소수점3째이하까지 표시, 빈자리는 공백으로 채워짐
print("금액 =", format(10000, "10d"))        #10자리수, 빈자리는 공백, d는 10진수
print("금액 =", format(125000, "3,d"))        #3자리뒤에 ,표시, d는 10진수

# (5) 양식문자 인수 : print( "%양식문자" %(값) )
name = "홍길동"
age = 35
price = 123.456
print("이름 : %s, 나이 : %d, data = %.2f" % (name, age, price))

# p47 (6) 외부 상수 인수
print("이름 : {}, 나이 : {}, data={}".format(name, age, price))
print("이름 : {1}, 나이 : {0}, data={2}".format(age, name, price))

# (7) format 축약형(SQL문 작성)
uid = input("id input : ")
query = f"select * from member where uid = {uid}"
print(query)  # member 테이블에서 uid가 hong인 레코드 검색




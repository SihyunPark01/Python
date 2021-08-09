# p39
num1 = 100
num2 = 20

add = num1 + num2
print('add=', add )
sub = num1 - num2
print(sub)
mul = num1 * num2
print(mul)
div = num1 / num2
print(div)
div2 = num1 % num2
print(div2)
square = num1**2   #제곱 계산
print(square)


#p40 (1) 동등비교
bool_result = num1 == num2
print(bool_result)
bool_result = num1 != num2
print(bool_result)

# (2) 크기비교
bool_result = num1 > num2
print(bool_result)

bool_result = num1 >= num2
print(bool_result)

bool_result = num1 < num2
print(bool_result)

bool_result = num1 <= num2
print(bool_result)


#p41 (1) 변수에 값 할당
i = tot = 10
i += 1
tot += i
print(i, tot)

# 같은 줄에 중복 출력
print('출력1', end=' , ')
print('출력2')
v1, v2 = 100, 200

# (2) 변수 교체
v2, v1 = v1, v2
print(v1,v2)

#(3) 패킹 할당
lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print(v1, v2)

*v1, v2 = lst
print(v1, v2)
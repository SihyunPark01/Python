#문자열 유형
oneLine = "this is one line string"
print(oneLine)

multiLine = """this is
multi line
string"""
print(multiLine)

multiLine2 = "this is\nmulti line\nstring"
print(multiLine2)

# (1) 문자열 색인
string = "PYTHON"
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

# (2) 문자열 연산
print("python" + " program") # 결합연산자
print("python-" + str(3.7) + ".exe") # 이때 3.7은 숫자가 아니라 문자열이므로 저렇게 담아줘야 함

print("-"*30) #반복연산자 : "반복할문자"*몇회

# (1) 왼쪽 기준
print(oneLine)
print("문자열 길이 : ", len(oneLine) )
print(oneLine[0 : 4])
print(oneLine[ : 4])
print(oneLine[ : ])
print(oneLine[:: 2]) #2의 배수 인덱스만 나옴

# (2) 오른쪽 기준
print(oneLine[0:-1:2]) #왼쪽처음부터 오른쪽끝이전까지 2씩 증가하여 슬라이싱
print(oneLine[-6:-1]) #오른쪽 맨끝을 기준으로 6번째 문자부터 마지막 문자 이전까지 슬라이싱
print(oneLine[-6:])  #오른쪽 맨끝을 기준으로 6번째 문자부터 마지막 문자까지 슬라이싱

# (3) 부분 문자열 생성
subString = oneLine[-11: ]
print(subString)

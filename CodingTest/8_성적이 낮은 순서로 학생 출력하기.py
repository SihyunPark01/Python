"""
날짜 : 2021/09/03
이름 : 박시현
내용 : 코딩테스트 - 성적이 낮은 순서로 학생 출력하기
"""
n = int(input())

dataset = []
for i in range(n):
    a, b = input().split()

    student = [a, int(b)]
    dataset.append(student)

# print(dataset)
scores = []
for i in range(len(dataset)):
    score = dataset[i][1]
    scores.append(score)

scores.sort()

names = []
for score in scores:
    for i, data in enumerate(dataset):
        if score == data[1]:
            names.append(data[0])
            dataset.pop(i)

print(names)

"""
# sort함수의 key 매개변수를 이용한 방법
import sys
list=[]
n= int(sys.stdin.readline())
for i in range(n):
    m= sys.stdin.readline().split()
    list.append(m)
list.sort(key=lambda x:x[1])
for i in list:
    print(i[0],end=' ')
"""
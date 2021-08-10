"""
날짜 : 2021/08/10
이름 : 박시현
내용 : 파이썬 자료구조 List 실습하기 교재 p84
"""

#List
list1 = [1, 2, 3, 4, 5]
print('list1 type :', type(list1))
print('list1[0] :', list[0])
print('list1[2] :', list[2])
print('list1[3] :', list[3])

list2 = [5, 3.14, True, 'Apple']
print('list2 type : ', type(list2))
print('list2[1] :', list2[1])
print('list2[2] :', list2[2])
print('list2[3] :', list2[3])

list3 = [[1,2,3],
         [4,5,6],
         [7,8,9]] #자바에서 2차원배열이라고 부르는 list안의 list

print('list3 type :', type(list3))
print('list3[0][0] :', list3[0][0])
print('list3[1][1] :', list3[1][1])
print('list3[2][0] :', list3[2][0])


#List 덧셈
ani1 = ['사자', '호랑이', '곰']
ani2 = ['코끼리', '기린']
ani3 = ani1 + ani2
print('ani3 :', ani3)


#List 수정, 삭제
nums = [1, 2, 3, 4, 5]
print('nums :', nums)

nums[1] = 7
print('nums :', nums)

nums[2:4] = [8, 9, 10]  #인덱스번호 2번과 3번
print('nums :', nums)

nums[3:5] = []
print('nums :', nums)

#List 반복문
array = [1,2,3,4,5]

for n in array:
    print('n :', n)

people = ['김유신','김춘추','장보고']
for person in people:
    print(person)

for i, value in enumerate(people):
    print('people[%d] : %s' % (i, value))


#List Comprehension
numbers = [1, 2, 3, 4, 5]

res1 = [ num * 3 for num in numbers]        #3을 곱한 수들을 배열로!
res2 = [ num * 3 for num in numbers if num % 2 == 1]        #홀수일때만 3을곱하라

print('res1 :', res1)
print('res2 :', res2)

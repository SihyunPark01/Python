"""
날짜 : 2021/09/17
이름 : 박시현
내용 : 코딩테스트 - 순차탐색
"""

# 순차탐색 함수
def sequential_search(dataset, target):
    pos = -1   #초기값, 인덱스값이 0부터 시작하니까 존재하지않는 -1로 잡아주는 것임.


    for i in range(len(dataset)):
        if dataset[i] == target:
            pos = i
            break

    return pos



dataset = [5, 10, 18, 22, 35, 55, 75, 103, 152]
value = int(input('검색할 숫자 : '))

pos = sequential_search(dataset, value)

if pos == -1:
    print('찾으시려는 숫자가 없습니다.')
else:
    print('%d는 %d번째에 있습니다.' % (value, pos))

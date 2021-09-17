"""
날짜 : 2021/09/03
이름 : 박시현
내용 : 코딩테스트 - 삽입정렬
"""
array = [4, 2, 1, 5, 3]

for i in range(1, len(array)):

    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            # swap - 일반적인 형태
            tmp = array[j-1]
            array[j-1] = array[j]
            array[j] = tmp

        else:
            break


    print('%d-round : %s' % (i, array))

print('최종결과 :', array)
"""
    날짜: 2021/08/12
    이름: 박시현
    내용: 파이썬 파일입출력 실습 교재 p217
"""

# 파일 읽기
file1 = open('./Test1.txt', 'r') #r이 읽어오는 read임
line = file1.readline()

print(line)
file1.close()

file2 = open('./Test1.txt', 'r')

while True:
    line = file2.readline()

    if not line: #파일내용이 더이상 없으면 빠져나가라
        break

    print('file2 line : ', line)

file2.close()


# 파일 쓰기
file3 = open('./Test2.txt', 'w', encoding='utf-8')
file3.write('안녕하세요.\n')
file3.write('반갑습니다.\n')
file3.write('감사합니다.\n')
file3.close()






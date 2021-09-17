"""
날짜 : 2021/09/03
이름 : 박시현
내용 : 코딩테스트 - 두 배열의 원소 교체
"""
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i] = b[i]
    else:
        break

print(sum(a))
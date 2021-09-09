


n, k = map(int, input().split())
result = 0

#일단 반복문을 떠올려라.
while True:

    if n == 1:
        break

    if n % k == 0:
        n /= k
    else:
        n -= 1

    result += 1

print(result)
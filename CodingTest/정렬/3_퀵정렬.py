"""
날짜 : 2021/09/03
이름 : 박시현
내용 : 코딩테스트 - 퀵정렬
"""
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피봇보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[pivot] >= array[left]:
            left += 1

        # 피봇보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[pivot] <= array[right]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽과 오른쪽 각각 다시 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array)-1)
print(array)
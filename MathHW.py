# BOJ 2870
import re


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


N = int(input())
TrashList = [input() for _ in range(N)]
# N = 6
# TrashList = ['43silos0', 'zita002', 'le2sim', '231233', '43', '503']

selectedNums = []
for _ in range(N):
    NumsByLine = list(map(int, re.findall("\d+", TrashList[_])))
    selectedNums.extend(NumsByLine)

selectedNums = quick_sort(selectedNums)
print(*selectedNums, sep="\n")
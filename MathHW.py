# BOJ 2870
import re
import heapq

N = int(input())
TrashList = [input() for _ in range(N)]
# N = 6
# TrashList = ['43silos0', 'zita002', 'le2sim', '231233','43','503']

selectedNums = []
for _ in range(N):
    NumsByLine = list(map(int, re.findall("\d+", TrashList[_])))
    for i in range(len(NumsByLine)):
        heapq.heappush(selectedNums, NumsByLine[i])

sortedNums = []
while selectedNums:
    sortedNums.append(heapq.heappop(selectedNums))

print(*sortedNums, sep="\n")

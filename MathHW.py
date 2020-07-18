# BOJ 2870
import re

# N = int(input())
# TrashList = [input() for _ in range(N)]
N = 4
TrashList = ['43silos0', 'zita002', 'le2sim', '231233']

selectedNums = []
for _ in range(N):
    NumsByLine = list(map(int, re.findall("\d+", TrashList[_])))
    selectedNums.extend(NumsByLine)

selectedNums.sort()
print(*selectedNums, sep="\n")

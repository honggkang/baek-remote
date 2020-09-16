# BOJ 11404

import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

costInfo = [list(map(int, input().split())) for _ in range(m)]  # source, destination, cost
inf = 1e9

Mx = [[inf]*n for _ in range(n)]

for _ in range(n):
    Mx[_][_] = 0

for _ in range(m):
    Mx[costInfo[_][0]-1][costInfo[_][1]-1] = min(Mx[costInfo[_][0]-1][costInfo[_][1]-1], costInfo[_][2])

for idx in range(n):  # 0~n-1, via idx
    L = list(range(0, n))  # 0~n-1
    L.pop(idx)
    for jdx in L:
        for kdx in range(n):
            Mx[jdx][kdx] = min(Mx[jdx][kdx], Mx[jdx][idx]+Mx[idx][kdx])

for col in range(n):
    for row in range(n):
        if Mx[row][col] == inf:
            Mx[row][col] = 0

for _ in range(n):
    print(*Mx[_])
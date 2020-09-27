# BOJ 15686

import sys
from collections import deque

input = sys.stdin.readline

def ch_dist(c1, c2):
    return abs(c1[1] - c2[1]) + abs(c1[0] - c2[0])


def minDist(num_store, sto, dM, sel):
    global ans
    sel[sto[0]][sto[1]] = True
    num_store += 1
    for y, x in hoCoord:
        dM[y][x] = min(ch_dist([y, x], sto), dM[y][x])
    if num_store == M:
        ans = min(ans, sum(sum(dM, [])))
        return
    else:
        for i in range(L):
            st = [chCoord[i][0], chCoord[i][1]]
            if not sel[st[0]][st[1]]:
                minDist(num_store, st, dM, sel)

N, M = map(int, input().split())
cityMap = [list(map(int, input().split())) for _ in range(N)]

selected = [[False]*N for _ in range(N)]
distMap = [[0]*N for _ in range(N)]
ans = 1e9

chCoord = []  # chicken store coordinate
hoCoord = []  # home coordinate

for y_ in range(N):
    for x_ in range(N):
        if cityMap[y_][x_] == 2:
            chCoord.append([y_, x_])
        elif cityMap[y_][x_] == 1:
            hoCoord.append([y_, x_])

L = len(chCoord)

# if len(chCoord) <= M:
#     pass  # yes !
# else:

# if numStore >= M:
# if number of chicken stores in cityMap <= M return sum chicken store
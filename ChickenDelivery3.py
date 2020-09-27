# BOJ 15686

import sys
from itertools import combinations

input = sys.stdin.readline

def ch_dist(c1, c2):
    return abs(c1[1] - c2[1]) + abs(c1[0] - c2[0])


N, M = map(int, input().split())
cityMap = [list(map(int, input().split())) for _ in range(N)]


chCoord = []  # chicken store coordinate
hoCoord = []  # home coordinate

for y_ in range(N):
    for x_ in range(N):
        if cityMap[y_][x_] == 2:
            chCoord.append([y_, x_])
        elif cityMap[y_][x_] == 1:
            hoCoord.append([y_, x_])

cL = len(chCoord)
hL = len(hoCoord)

Dict = [[1e9]*cL for _ in range(hL)]  # len(hoCoord) x len(chCoord)

for hi in range(hL):
    for ci in range(cL):
        Dict[hi][ci] = ch_dist(hoCoord[hi], chCoord[ci])

sol = []
if len(chCoord) <= M:
    temp = [min(Dict[_]) for _ in range(hL)]
    sol = sum(temp)
    print(sol)
else:
    opt = list(range(cL))  # 0~cL-1
    chComb = list(combinations(opt, M))  # M out of cL
    for c in range(len(chComb)):
        temp = [[Dict[r][_] for _ in chComb[c]] for r in range(hL)]
        temin = [min(temp[_]) for _ in range(hL)]
        sol.append(sum(temin))
    print(min(sol))

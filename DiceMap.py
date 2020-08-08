import sys
import copy as cp
global N, M


def map_check(x, y, c):
    if c == 4:
        x_new = x+1
        y_new = y
    elif c == 3:
        x_new = x-1
        y_new = y
    elif c == 2:
        y_new = y-1
        x_new = x
    else:
        y_new = y+1
        x_new = x
    if 0 <= x_new < N and 0 <= y_new < M:
        return x_new, y_new, True
    else:
        return x, y, False

input = sys.stdin.readline
N, M, x, y, K = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Commands = list(map(int, input().split()))
# N = 4
# M = 2
# x = 0
# y = 0
# K = 8
# Map = [[0, 2], [3, 4], [5, 6], [7, 8]]
# Commands = [4, 4, 4, 1, 3, 3, 3, 2]

nD = [[0]*2 for _ in range(3)] # now Dice

for c in Commands:
    x, y, flag = map_check(x, y, c)
    pD = cp.deepcopy(nD)
    if flag:
        if c == 4:  # south
            nD[0][0] = pD[2][0]
            nD[2][0] = pD[0][1]
            nD[0][1] = pD[2][1]
            if Map[x][y] == 0:
                nD[2][1] = pD[0][0]
                Map[x][y] = nD[2][1]
            else:
                nD[2][1] = Map[x][y]
                Map[x][y] = 0
        elif c == 3:  # north
            nD[2][0] = pD[0][0]
            nD[0][0] = pD[2][1]
            nD[0][1] = pD[2][0]
            if Map[x][y] == 0:
                nD[2][1] = pD[0][1]
                Map[x][y] = nD[2][1]
            else:
                nD[2][1] = Map[x][y]
                Map[x][y] = 0
        elif c == 2:  # west
            nD[2][0] = pD[1][0]
            nD[1][0] = pD[2][1]
            nD[1][1] = pD[2][0]
            if Map[x][y] == 0:
                nD[2][1] = pD[1][1]
                Map[x][y] = nD[2][1]
            else:
                nD[2][1] = Map[x][y]
                Map[x][y] = 0
        else:  # east
            nD[1][0] = pD[2][0]
            nD[2][0] = pD[1][1]
            nD[1][1] = pD[2][1]
            if Map[x][y] == 0:
                nD[2][1] = pD[1][0]
                Map[x][y] = nD[2][1]
            else:
                nD[2][1] = Map[x][y]
                Map[x][y] = 0
        print(nD[2][0])
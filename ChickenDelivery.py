# BOJ 15686

import sys
from collections import deque

input = sys.stdin.readline

def ch_dist(c1, c2):
    return abs(c1[1] - c2[1]) + abs(c1[0] - c2[0])


def bfs(queue,visited):
    l = len(queue)
    if l:
        x, y = queue.popleft()
        for _ in range():
            for dy, dx in (0,-1), (0,1), (-1,0), (1,0):
                if -1 < x+dx < N and -1< y+dx < N and not visited[y+dy][x+dx]:
                    queue.append([y+dy,x+dx])
                    if cityMap[y][x] == 2  # chicken store
                        return [y, x]
        bfs(queue,visited)
    else:
        print('no chicken store')


N, M = map(int, input().split())
cityMap = [list(map(int, input().split())) for _ in range(N)]

visited = [[False]*N for _ in range(N)]
Q4B = deque([])

numStore = 0
chCoord = []

for _ in range(M):
    num = cityMap[_].count(2)
    if num:
        chCoord.append([_, cityMap[_].index(2)])
        numStore += num

if numStore >= M:
# if number of chicken stores in cityMap <= M return sum chicken store
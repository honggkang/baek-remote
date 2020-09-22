# BOJ 1916

import sys


input = sys.stdin.readline
inf = 1e10

N = int(input())  # of cities
M = int(input())  # of buses
costInfo = [list(map(int, input().split())) for _ in range(M)]  # source, destination, cost
S, D = map(int, input().split())  # source, destination

dis = [inf]*(N+1)
visited = [False]*(N+1)

interIndex = S
dis[interIndex] = 0
visited[interIndex] = True

indexInfo = []
for _ in range(N):
    indexInfo.append([])

for i in range(M):
    for j in range(N):
        if costInfo[i][0] == j+1:
            indexInfo[j].append(i)

# [[0, 1, 2, 3], [4], [5, 6], [7], [], [], [], []]

while sum(visited) != N:
    temp = []

    for i in indexInfo[interIndex-1]:
        dis[costInfo[i][1]] = min(dis[costInfo[i][1]], dis[interIndex] + costInfo[i][2])

    min_temp = 1e10
    interIndex = False
    for j in range(1, N+1):  # 1~N
        if not visited[j] and min_temp > dis[j]:
            min_temp = dis[j]
            interIndex = j

    if not interIndex:
        break
    visited[interIndex] = True


print(dis[D])
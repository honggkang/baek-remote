# BOJ 1916

import sys


input = sys.stdin.readline
inf = 1e5

N = int(input())  # of cities
M = int(input())  # of buses
costInfo = [list(map(int, input().split())) for _ in range(M)]  # source, destination, cost
S, D = map(int, input().split())  # source, destination

dis = [inf]*(N+1)
visited = [False]*(N+1)

interIndex = S
dis[interIndex] = 0
visited[interIndex] = True

while sum(visited) != N:
    temp = []
    for i in range(N):
        if costInfo[i][0] == interIndex:
            dis[costInfo[i][1]] = min(dis[costInfo[i][1]], dis[interIndex] + costInfo[i][2])
            temp.append(dis[costInfo[i][1]])
    min_temp = min(temp)

    temp_dis = dis.copy()
    interIndex = temp_dis.index(min_temp)
    while visited[interIndex]:
        temp_dis.pop(interIndex)
        interIndex = temp_dis.index(min_temp)
    visited[interIndex] = True



print(dis)
# BOJ 6086
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # of room
# N = 6
flow_map = [list(input().split()) for _ in range(N)]
# flow_map = [['A', 'B', '3'], ['B', 'A', '5'], ['B', 'C', '3'], ['C', 'D', '5'], ['D', 'Z', '4'], ['B', 'Z', '6']]
flow_cap = dict()
flow = dict()
for i in range(N):
    s = flow_map[i][0]
    d = flow_map[i][1]

for i in range(N):
    s = flow_map[i][0]
    d = flow_map[i][1]
    if s > d:
        s, d = d, s
    v = int(flow_map[i][2])
    try:
        flow_cap[s]
    except KeyError:
        flow_cap[s] = dict()
    try:
        flow_cap[s][d] += v
    except KeyError:
        flow_cap[s][d] = v

        try:
            flow[s][d] = 0
        except KeyError:
            flow[s] = dict()
            flow[s][d] = 0
        try:
            flow[d][s] = 0
        except KeyError:
            flow[d] = dict()
            flow[d][s] = 0

temp = dict()
for i in flow_cap.keys():
    temp[i] = flow_cap[i].copy()

for i in temp.keys():
    for j in temp[i].keys():
        try:
            flow_cap[j][i] = temp[i][j]
        except KeyError:
            flow_cap[j] = dict()
            flow_cap[j][i] = temp[i][j]

src = 'A'
goal = 'Z'

while True:
    prev = dict()
    min_flow = dict()
    for keys in flow:
        prev[keys] = -1
        min_flow[keys] = 1e9

    prev[src] = 0

    dq = deque()
    dq.append(src)
    flag = False
    while dq:
        start = dq.popleft()
        for destination in flow[start].keys():
            if flow[start][destination] < flow_cap[start][destination] and prev[destination] == -1:
                prev[destination] = start
                min_flow[destination] = flow_cap[start][destination]-flow[start][destination]
                dq.append(destination)
                if destination == goal:
                    flag = True
                    break
            if flag:
                break

    if flag:
        backf = min_flow[goal]
        back = prev[goal]
        count = 1
        while back != src:
            if back == -1:
                print('shit')
            backf = min(backf, min_flow[back])
            back = prev[back]
            count += 1

        dest = goal
        star = prev[dest]
        for i in range(count):
            flow[star][dest] += backf
            flow[dest][star] -= backf
            dest = star
            star = prev[dest]
    else:
        temp = 0
        for keys in flow[goal]:
            temp -= flow[goal][keys]
        print(temp)
        break
#     print(dq)

# for c in flow[src].keys()
#     if c == 'Z':
#         return 1
#     else:
#
#     if flow[src][c] < flow_cap[src][c]:
#         dq.append(c)
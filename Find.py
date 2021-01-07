# BOJ 11725
import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  # of nodes
# N = 7
p = {}
Q = deque([1])  # default root

Mc = [list(map(int, input().split())) for _ in range(N-1)]  # group of linked nodes
# Mc = [[1, 6], [6, 3], [3, 5], [4, 1], [2, 4], [4, 7]]
Mct = [list(x) for x in zip(*Mc)]
idx = 0
Graph = {}
for _ in range(1,N+1):
    Graph[_] = []

for _ in range(N-1):
    x, y = Mc[_]
    Graph[x].append(y)
    Graph[y].append(x)

while Q:
    pa_node = Q.popleft()
    for ch_node in Graph[pa_node]:
        p[ch_node] = pa_node
        tdx = Graph[ch_node].index(pa_node)
        Graph[ch_node].pop(tdx)
        Q.append(ch_node)

for _ in range(2, N+1):
    print(p[_])
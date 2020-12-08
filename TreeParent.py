# BOJ 11725
import sys
from collections import deque

input = sys.stdin.readline

# N = int(input())  # of nodes
N = 7
p = {}
Q = deque([1])  # default root

# Mc = [list(map(int, input().split())) for _ in range(N-1)]  # group of linked nodes
Mc = [[1, 6], [6, 3], [3, 5], [4, 1], [2, 4], [4, 7]]
Mct = [list(x) for x in zip(*Mc)]
idx = 0

while Q:
    node = Q.popleft()
    nu = Mct[0].count(node)+Mct[1].count(node)
    for _ in range(nu):
        try:
            ni = Mct[idx].index(node)  # node index that has parent node 'node'
        except ValueError:
            idx = 1-idx
            ni = Mct[idx].index(node)  # node index that has parent node 'node'
        nv = Mct[1-idx][ni]  # node val. that has parent node 'node'
        Mct[idx].pop(ni)
        Mct[1-idx].pop(ni)
        p[nv] = node
        Q.append(nv)

for _ in range(2, N+1):
    print(p[_])

# BOJ 1922

import sys

input = sys.stdin.readline


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, u):
    root1 = find(v)
    root2 = find(u)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2

            if rank[root1] == rank[root2]:
                rank[root2] += 1


N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]

for _ in range(M):
    edges[_][2], edges[_][0] = edges[_][0], edges[_][2]

edges.sort()

# make set
parent = [i for i in range(N)]
rank = [0]*N
mst = []

for edge in edges:
    weight, v, u = edge
    v -= 1
    u -= 1
    if find(v) != find(u):
        union(v, u)
        mst.append(edge)

temp = 0
for _ in range(N-1):
    temp += mst[_][0]

print(temp)
# BOJ 13458
import sys


input = sys.stdin.readline

# N = int(input())  # of room
N = 6
# flow_map = [list(input().split()) for _ in range(N)]
flow_map = [['A', 'B', '3'], ['B', 'A', '5'], ['B', 'C', '3'], ['C', 'D', '5'], ['D', 'Z', '4'], ['B', 'Z', '6']]
map = [[0]*52 for _ in range(52)] #
flow_dic = dict()
for i in range(N):
    s = flow_map[i][0]
    d = flow_map[i][1]
    if s > d:
        s, d = d, s
    v = int(flow_map[i][2])
    try:
        flow_dic[s][d] += v
    except KeyError:
        flow_dic[s] = dict()
        flow_dic[s][d] = v


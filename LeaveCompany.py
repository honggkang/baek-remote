import sys

input = sys.stdin.readline

N = int(input())
TimePrice = [list(map(int, input().split())) for _ in range(N)]
# N = 7
# TimePrice = [[3, 10], [5, 20], [1, 10], [1, 20], [2, 15], [4, 40], [2, 200]] # day-1 + T[day-1] = day
# (ex) 0 + T[0] (schedule 1) = 3, 2 + T[2] (schedule 3) = 3
V = [0]*(N+1) # V[0]: meaningless, V[1]~V[N]
# V[day] = V[day-i] + TimePrice[day-i][1]
checkSchedule = []

for d in range(1, N+1):
    temp = checkSchedule.copy()
    checkSchedule = []
    for c in temp:
        if c-1 + TimePrice[c-1][0] == d:
            V[d] = max(V[d], V[c-1] + TimePrice[c-1][1])
        else:
            checkSchedule.append(c)
    if d-1 + TimePrice[d-1][0] == d:
        V[d] = max(V[d], V[d-1] + TimePrice[d-1][1])
    else:
        checkSchedule.append(d)
    if V[d] == 0 or V[d]<V[d-1]:
        V[d] = V[d-1]

print(V[-1])
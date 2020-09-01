# BOJ 13458
import sys


input = sys.stdin.readline

N = int(input())  # of room
A = list(map(int, input().split()))  # of people being tested
BC = list(map(int, input().split()))

DirNum = 0
for _ in range(N):
    temp = A[_] - BC[0]
    if temp < 0:
        pass
    else:
        temp2 = temp % BC[1]
        if temp2:
            DirNum += temp//BC[1]+1
        else:
            DirNum += temp//BC[1]

print(DirNum+N)
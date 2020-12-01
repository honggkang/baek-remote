# BOJ 9461
import sys

input = sys.stdin.readline

T = int(input())
N = [int(input()) for _ in range(T)]
Pado = {1:1, 2:1, 3:1, 4:2, 5:2}

def getValue(n):
    try:
        return Pado[n]
    except:
        res = getValue(n-1) + getValue(n-5)
        Pado[n] = res
        return Pado[n]

for i in range(T):
    print(getValue(N[i]))
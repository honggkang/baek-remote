# BOJ 3761

import sys
from queue import PriorityQueue  # further work

input = sys.stdin.readline
tn = int(input())
n = int(input())
names = list(input().split())  # male (name: lower) & female (name: upper)
mName = names[0:n]
fName = names[n:2*n]
mName.sort()
fName.sort()

prefList = [[0]*n for _ in range(2*n)]
# prefList[0][]~prfList[n-1][]: male pref. / prefList[n][]~prefList[2n-1][]: female pref.

for _ in range(2*n):
    temp = input()
    idx = names.index(temp[0])
    for p in range(n):
        prefList[idx][p] = temp[p+2]

mPrefList = prefList[0:n]
fPrefList = prefList[n:2*n]

boy = [False]*n  # if boy has his girl

fQ = [[] for _ in range(n)]  # candidate of candidate
fC = []*n  # candidate
fR = [n]*n  # rank value initialize (rank: 0~n-1)


def matching(fpl, fq):
    l = len(fq)
    if l == 1:
        for i in range(n):
            if fpl[i] == fq[0]:
                return fq[0], i
    elif l >= 2:
        for i in range(n):
            for li in range(l):
                if fpl[i] == fq[li]:
                    return fq[li], i
    else:
        print('no matching')


for i in range(n):
    for fqi in range(n):
        if fQ[fqi]:
            c, r = matching(fPrefList[fqi], fQ[fqi])  # candidate and rank
            if fR[fqi] > r:
                fR[fqi] = r
                fC[fqi] = c
    if sum(boy) == n:
        break

print(fC)
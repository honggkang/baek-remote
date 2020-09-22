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

maleSingle = list(range(0, n))
mList = [[] for _ in range(n)]  # deterministic wife, mList[0]: male of female 0

tempList = [[] for _ in range(n)]  # male candidates,

pidx = -1
while maleSingle:
    pidx += 1
    for _ in maleSingle:
        tempList[fName.index(mPrefList[_][pidx])].append(mName[_])  # who wants girl? male candidates

    for idx in range(n):
        maleNum = len(tempList[idx])
        if maleNum == 1:
            mList[idx].append(tempList[idx][0])
            maleSingle.pop(mName.index(mList[idx][0]))
        elif maleNum >= 2:
            brf = False
            for fdx in range(n):
                for mdx in range(maleNum):
                    if tempList[idx][mdx] in fPrefList[idx][fdx]:
                        mList[idx].append(tempList[idx][mdx])
                        maleSingle.pop(mName.index(mList[idx][0]))
                        brf = True
                        break
                if brf:
                    break

print(mList)
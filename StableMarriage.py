# BOJ 3761

import sys

input = sys.stdin.readline
tn = int(input())

ans_fName = []
ans_mName = []
ans_fC = []

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


for testi in range(tn):
    n = int(input())
    names = list(input().split())  # male (name: lower) & female (name: upper)
    names.sort()
    mName = names[n:2*n]
    fName = names[0:n]

    prefList = [[0]*n for _ in range(2*n)]
    # prefList[0][]~prfList[n-1][]: male pref. / prefList[n][]~prefList[2n-1][]: female pref.

    for _ in range(2*n):
        temp = input()
        idx = names.index(temp[0])
        for p in range(n):
            prefList[idx][p] = temp[p+2]

    mPrefList = prefList[n:2*n]
    fPrefList = prefList[0:n]

    boy = [False]*n  # if boy has his girl

    fC = [[] for _ in range(n)]  # candidate
    fR = [n]*n  # rank value initialize (rank: 0 ~ n-1)

    bfi = [0]*n

    while sum(boy) != n:
        fQ = [[] for _ in range(n)]  # candidate of candidate
        for j in range(n):
            if not boy[j]:
                i = bfi[j]
                bfi[j] += 1
                wc = mPrefList[j][i]  # wife candidate
                fQ[fName.index(wc)].append(mName[j])

        for fqi in range(n):
            if fQ[fqi]:
                c, r = matching(fPrefList[fqi], fQ[fqi])  # candidate and rank
                if fR[fqi] > r:
                    boy[mName.index(c)] = True
                    # print(c)
                    # print(fName[fqi])
                    if fC[fqi]:
                        boy[mName.index(fC[fqi])] = False
                    fR[fqi] = r
                    fC[fqi] = c

    ans_fName.append(fName)
    ans_mName.append(mName)
    ans_fC.append(fC)


for ti in range(tn):
    for _ in range(n):
        print(ans_mName[ti][_], ans_fName[ti][ans_fC[ti].index(mName[_])])
    print('\n')
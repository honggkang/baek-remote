# BOJ 2064
import sys

input = sys.stdin.readline
n = int(input())

S = [list(map(int, input().split('.'))) for _ in range(n)]  # group of linked nodes

if n != 1:
    for g in range(4):  # IP 구분 (4-byte)
        tmp = []
        for u in range(n):  # users (hosts)
            tmp.append(S[u][g])

        mm = min(tmp)
        MM = max(tmp)
        if mm != MM:
            break

    l = len(bin(MM^mm)) - 2

    L = 2**l
    # aa = MM - L + 1
    # aa = 2**8 - 2**l
    xx = '00000000'
    ll = 10-len(bin(MM))
    aa = int('0b' + xx[0:ll] + bin(MM)[2:10-l-ll] + xx[0:l], 2)

    ##
    for _ in range(g):
        print('{}.'.format(S[0][_]), end='')
    if g != 3:
        print('{}.'.format(aa), end='')
    else:
        print(aa)

    for _ in range(3-g):
        if _ != 2-g:
            print('0.', end='')
        else:
            print('0')
    ##

    ##
    x = 255
    y = 255 - L + 1
    for _ in range(g):
        print('{}.'.format(x), end='')
    if g != 3:
        print('{}.'.format(y), end='')
    else:
        print(y)

    for _ in range(3-g):
        if _ != 2-g:
            print('0.', end='')
        else:
            print('0')
    ##
else:
    print('{}.{}.{}.{}'.format(S[0][0],S[0][1],S[0][2],S[0][3]))
    print('255.255.255.255')
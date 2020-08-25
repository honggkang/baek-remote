# BOJ 9251
# import sys

# input = sys.stdin.readline

s1 = input()
s2 = input()
# s1 = 'ACAYKP\n'
# s2 = 'CAPCAK\n'
# s1 = 'ACAYKP'
# s2 = 'CAPCAK'

N1 = len(s1)
N2 = len(s2)
table = [[0]*(N2+1) for _ in range(N1+1)]

for i in range(N1):
    for j in range(N2):
        if s1[i] == s2[j]:
            table[i+1][j+1] = table[i][j]+1
        else:
            table[i+1][j+1] = max(table[i][j+1], table[i+1][j])

print(table[-1][-1])
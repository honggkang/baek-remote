import sys

input = sys.stdin.readline
N, K = map(int, input().split())
# items = [list(map(int, input().split())) for _ in range(N)]  # weight, value

# N = 6
# K = 9
# items = [[3, 6], [2, 7], [4, 6], [4, 2], [4, 10], [1, 5]] # [][0]: weight, [][1]: value

# N = 4
# K = 5
# items = [[1, 4], [1, 8], [3, 3], [4, 8]]
# # ans = 16

# N = 10
# K = 10
# items = [[1, 2], [4, 9], [1, 5], [4, 8], [4, 1], [1, 7], [3, 2], [3, 7], [2, 5], [5, 2]]

matrixDP = [[0 for col in range(K+1)] for row in range(N+1)] # 1~K, 1~N

for it in range(1, N + 1):
    itemWeight, itemValue = map(int, input().split())
    for w in range(1, K+1):
        if w - itemWeight >= 0:
            matrixDP[it][w] = max(matrixDP[it-1][w-itemWeight] + itemValue, matrixDP[it-1][w])
        else:
            matrixDP[it][w] = matrixDP[it-1][w]

print(matrixDP[-1][-1])
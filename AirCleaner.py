import sys
import math

input = sys.stdin.readline


def matrix_addition(A, B):
    """
    Adds two matrices and returns the sum
        :param A: The first matrix
        :param B: The second matrix

        :return: Matrix sum
    """
    rowsA = len(A)
    colsA = len(A[0])
    # rowsB = len(B)
    # colsB = len(B[0])
    # if rowsA != rowsB or colsA != colsB:
    #     raise ArithmeticError('Matrices are NOT the same size.')

    C = [[0]*colsA for _ in range(rowsA)]

    for i in range(rowsA):
        for j in range(colsA):
            C[i][j] = A[i][j] + B[i][j]

    return C


def diffusion(dust_map, arr4, arr3, arr2):
    new_dust_map = [[0]*C for _ in range(R)]
    for c in arr4:
        val = math.floor(dust_map[c[0]][c[1]]/5)
        new_dust_map[c[0]][c[1]] -= 4*val
        new_dust_map[c[0]-1][c[1]] += val
        new_dust_map[c[0]+1][c[1]] += val
        new_dust_map[c[0]][c[1]-1] += val
        new_dust_map[c[0]][c[1]+1] += val
    for di in arr3:
        if di == 'up':
            for idx in range(len(arr3[di])):
                pos = arr3[di][idx]
                val = math.floor(dust_map[pos[0]][pos[1]]/5)
                new_dust_map[pos[0]][pos[1]] -= 3*val
                new_dust_map[pos[0]+1][pos[1]] += val
                new_dust_map[pos[0]][pos[1]-1] += val
                new_dust_map[pos[0]][pos[1]+1] += val
        elif di == 'down':
            for idx in range(len(arr3[di])):
                pos = arr3[di][idx]
                val = math.floor(dust_map[pos[0]][pos[1]]/5)
                new_dust_map[pos[0]][pos[1]] -= 3*val
                new_dust_map[pos[0]-1][pos[1]] += val
                new_dust_map[pos[0]][pos[1]-1] += val
                new_dust_map[pos[0]][pos[1]+1] += val
        elif di == 'right':
            for idx in range(len(arr3[di])):
                pos = arr3[di][idx]
                val = math.floor(dust_map[pos[0]][pos[1]]/5)
                new_dust_map[pos[0]][pos[1]] -= 3*val
                new_dust_map[pos[0]+1][pos[1]] += val
                new_dust_map[pos[0]-1][pos[1]] += val
                new_dust_map[pos[0]][pos[1]-1] += val
        else:  # left
            for idx in range(len(arr3[di])):
                pos = arr3[di][idx]
                val = math.floor(dust_map[pos[0]][pos[1]]/5)
                new_dust_map[pos[0]][pos[1]] -= 3*val
                new_dust_map[pos[0]+1][pos[1]] += val
                new_dust_map[pos[0]-1][pos[1]] += val
                new_dust_map[pos[0]][pos[1]+1] += val
    for c in arr2:
        val = math.floor(dust_map[c[0]][c[1]]/5)
        new_dust_map[c[0]][c[1]] -= 2*val
        for yi, xi in (-1, 0), (1, 0), (0, -1), (0, 1):
            y = c[0]+yi
            x = c[1]+xi
            if -1 < y < R and -1 < x < C and [y, x] != [y1, 0] and [y, x] != [y2, 0]:
                new_dust_map[y][x] += val
    return matrix_addition(new_dust_map, dust_map)


def circulate(dust_map):
    new_dust_map = [[0]*C for _ in range(R)]
    for _ in range(R):
        new_dust_map[_] = dust_map[_].copy()

    for i in range(1, C):
        new_dust_map[0][i-1] = dust_map[0][i]
        new_dust_map[y1][i] = dust_map[y1][i-1]
    for i in range(1, y1+1):
        new_dust_map[i][0] = dust_map[i-1][0]
        new_dust_map[i-1][C-1] = dust_map[i][C-1]
    for i in range(1, C):
        new_dust_map[R-1][i-1] = dust_map[R-1][i]
        new_dust_map[y2][i] = dust_map[y2][i-1]
    for i in range(y2, R-1):
        new_dust_map[i][0] = dust_map[i+1][0]
        new_dust_map[i+1][C-1] = dust_map[i][C-1]
    new_dust_map[y1][0] = 0
    new_dust_map[y2][0] = 0
    return new_dust_map

R, C, T = map(int, input().split())
dustMap = [list(map(int, input().split())) for _ in range(R)]
mp = [] # (y1, 0), (y2, 0)
for _ in range(R):
    if dustMap[_][0] == -1:
        mp.append(_)
        dustMap[_][0] = 0

y1 = mp[0]
y2 = mp[1]
# (y,x)
dif2 = [[y1-1, 0], [y2+1, 0], [0, 0], [R-1, 0], [0, C-1], [R-1, C-1]]  # 2 way diffusion

dif3 = {'left': [], 'up': [], 'down': [], 'right': []}  # 3 way diffusion
for _ in range(1, y1-1):  # left-blocked
    dif3['left'].append([_, 0])
for _ in range(y2+2, R-1):  # left-blocked
    dif3['left'].append([_, 0])
dif3['left'].append([y1, 1])
dif3['left'].append([y2, 1])
for _ in range(1, R-1):
    dif3['right'].append([_, C-1])  # right-blocked
for _ in range(1, C-1):  # 1~C-2
    dif3['up'].append([0, _])  # up-blocked
    dif3['down'].append([R-1, _])  # down-blocked

dif4 = []  # 4 way diffusion
for _ in range(1, y1):
    dif4.append([_, 1])
for _ in range(y2+1, R-1):
    dif4.append([_, 1])
for i in range(2, C-1):
    for j in range(1, R-1):
        dif4.append([j, i])

for t in range(T):
    dustMap = diffusion(dustMap, dif4, dif3, dif2)
    dustMap = circulate(dustMap)

temp = 0
for i in range(R):
    temp = temp + sum(dustMap[i])

# for _ in range(R):
#     print(*dustMap[_])

print(temp)
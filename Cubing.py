# BOJ 5373

import sys
import copy as cp

input = sys.stdin.readline


def column(matrix, i):
    return [row[i] for row in matrix]


def column_input(col, matrix, i):
    for r in range(3):
        matrix[r][i] = col[r]
    return matrix



def rotate(face, dir):
    # face (2d array), direction, side array 1~4, CCW
    rotated_face = [[0] * 3 for _ in range(3)]
    if dir == '-':
        d = 1
    else:  # CW
        d = -1
    for i in range(3):  # x
        for j in range(3):  # y
            xf = d*(j-1)+1
            yf = -d*(i-1)+1
            rotated_face[xf][yf] = face[i][j]
    return rotated_face


tn = int(input())  # test case
# face: U D F B L R
# direction: + CW - CCW
# color: w y r o g b

for _ in range(tn):
    new_info = {'U': [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']],
                'D': [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']], \
                'F': [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']],
                'B': [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']], \
                'L': [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']],
                'R': [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]}
    n = int(input())  # input
    com = list(input().split())
    for i in range(n):
        info = cp.deepcopy(new_info)
        f = com[i][0]  # face
        dir = com[i][1]  # direction
        new_info[f] = rotate(info[f], dir)
        if f == 'U':
            # CCW
            if dir == '-':
                new_info['L'][2] = cp.deepcopy(info['B'][2])
                new_info['R'][2] = cp.deepcopy(info['F'][2])
                new_info['F'][2] = cp.deepcopy(info['L'][2])
                new_info['B'][2] = cp.deepcopy(info['R'][2])
            # CW
            else:
                new_info['L'][2] = cp.deepcopy(info['F'][2])
                new_info['R'][2] = cp.deepcopy(info['B'][2])
                new_info['F'][2] = cp.deepcopy(info['R'][2])
                new_info['B'][2] = cp.deepcopy(info['L'][2])
        elif f == 'D':
            # CCW
            if dir == '-':
                new_info['L'][0] = cp.deepcopy(info['F'][0])
                new_info['R'][0] = cp.deepcopy(info['B'][0])
                new_info['F'][0] = cp.deepcopy(info['R'][0])
                new_info['B'][0] = cp.deepcopy(info['L'][0])
            # CW
            else:
                new_info['L'][0] = cp.deepcopy(info['B'][0])
                new_info['R'][0] = cp.deepcopy(info['F'][0])
                new_info['F'][0] = cp.deepcopy(info['L'][0])
                new_info['B'][0] = cp.deepcopy(info['R'][0])
        elif f == 'F':
            # CCW
            if dir == '-':
                new_info['U'][0] = list(reversed(column(info['R'], 0)))
                new_info['D'][0] = column(info['L'], 2)
                new_info['L'] = column_input(info['U'][0], new_info['L'], 2)
                new_info['R'] = column_input(list(reversed(info['D'][0])), new_info['R'], 0)
            # CW
            else:
                new_info['U'][0] = column(info['L'], 2)
                new_info['D'][0] = list(reversed(column(info['R'], 0)))
                new_info['L'] = column_input(info['D'][0], new_info['L'], 2)
                new_info['R'] = column_input(list(reversed(info['U'][0])), new_info['R'], 0)
        elif f == 'B':
            # CCW
            if dir == '-':
                new_info['U'][2] = column(info['L'], 0)
                new_info['D'][2] = list(reversed(column(info['R'], 2)))
                new_info['L'] = column_input(info['D'][2], new_info['L'], 0)
                new_info['R'] = column_input(list(reversed(info['U'][2])), new_info['R'], 2)
            # CW
            else:
                new_info['U'][2] = list(reversed(column(info['R'], 2)))
                new_info['D'][2] = column(info['L'], 0)
                new_info['L'] = column_input(info['U'][2], new_info['L'], 0)
                new_info['R'] = column_input(list(reversed(info['D'][2])), new_info['R'], 2)
        elif f == 'L':
            # CCW
            if dir == '-':
                new_info['U'] = column_input(column(info['F'], 0), new_info['U'], 0)
                new_info['D'] = column_input(column(info['B'], 2), new_info['D'], 2)
                new_info['F'] = column_input(list(reversed(column(info['D'], 2))), new_info['F'], 0)
                new_info['B'] = column_input(list(reversed(column(info['U'], 0))), new_info['B'], 2)
            else:
                new_info['U'] = column_input(list(reversed(column(info['B'], 2))), new_info['U'], 0)
                new_info['D'] = column_input(list(reversed(column(info['F'], 0))), new_info['D'], 2)
                new_info['F'] = column_input(column(info['U'], 0), new_info['F'], 0)
                new_info['B'] = column_input(column(info['D'], 2), new_info['B'], 2)
        elif f == 'R':
            # CCW
            if dir == '-':
                new_info['U'] = column_input(list(reversed(column(info['B'], 0))), new_info['U'], 2)
                new_info['D'] = column_input(list(reversed(column(info['F'], 2))), new_info['D'], 0)
                new_info['F'] = column_input(column(info['U'], 2), new_info['F'], 2)
                new_info['B'] = column_input(column(info['D'], 0), new_info['B'], 0)
            else:
                new_info['U'] = column_input(column(info['F'], 2), new_info['U'], 2)
                new_info['D'] = column_input(column(info['B'], 0), new_info['D'], 0)
                new_info['F'] = column_input(list(reversed(column(info['D'], 0))), new_info['F'], 2)
                new_info['B'] = column_input(list(reversed(column(info['U'], 2))), new_info['B'], 0)

    for ii in range(3):
        pi = 2-ii
        print(*new_info['U'][pi], sep='')
    # print(new_info)




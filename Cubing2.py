# BOJ 5373

import sys

input = sys.stdin.readline


def column(matrix, i):
    return [row[i] for row in matrix]


def column_input(col, matrix, i):
    for r in range(3):
        matrix[r][i] = col[r]
    return matrix



def rotate(face, dir, sa1, sa2, sa3, sa4):
    # face (2d array), direction, side array 1~4, CCW
    rotated_face = face.copy()
    if dir == '-':
        d = -1
        sa1, sa2, sa3, sa4 = sa4, sa1, sa2, sa3
    else:
        d = 1
        sa1, sa2, sa3, sa4 = sa2, sa3, sa4, sa1
    for i in range(3):  # x
        for j in range(3):  # y
            xf = d*(j-1)+1
            yf = -d*(i-1)+1
            rotated_face[xf][yf] = face[i][j]
    return rotated_face, sa1, sa2, sa3, sa4


tn = int(input())  # test case
# face: U D F B L R
# direction: + CW - CCW
# color: w y r o g b

# tt[0]: self face, tt[1]~tt[4]: side arrays
upFace = [[['w','w','w'],['w','w','w'],['w','w','w']],\
      ['r','r','r'],['b','b','b'],['o','o','o'],['g','g','g']]  # side arrays (front, right, back, left)
downFace = [[['y','y','y'],['y','y','y'],['y','y','y']],\
      ['r','r','r'],['g','g','g'],['y','y','y'],['b','b','b']]  # side arrays (front, left, back, right)
leftFace = [[['g','g','g'],['g','g','g'],['g','g','g']],\
      ['r','r','r'],['w','w','w'],['o','o','o'],['y','y','y']]  # side arrays (front, up, back, down)
leftFace[1][0] = upFace[1][0]
rightFace = [[['w','w','w'],['w','w','w'],['w','w','w']],\
      ['r','r','r'],['b','b','b'],['y','y','y'],['g','g','g']]  # tt[0]: self face, tt[1]~tt[4]: side arrays



for _ in range(tn):
    info = {'U':[['w','w','w'],['w','w','w'],['w','w','w']], 'D':[['y','y','y'],['y','y','y'],['y','y','y']],\
            'F':[['r','r','r'],['r','r','r'],['r','r','r']], 'B':[['o','o','o'],['o','o','o'],['o','o','o']],\
            'L':[['g','g','g'],['g','g','g'],['g','g','g']], 'R':[['b','b','b'],['b','b','b'],['b','b','b']]}
    n = int(input())  # input
    com = list(input().split())
    for i in range(n):
        f = com[i][0]  # face
        dir = com[i][1]  # direction
        if f == 'U':
            leftArray = info['L'][2]
            rightArray = info['R'][2]
            frontArray = info['F'][2]
            backArray = info['B'][2]
            info[f], leftArray, frontArray, rightArray, backArray = rotate(info[f], dir, leftArray, frontArray, rightArray, backArray)
        elif f == 'D':
            leftArray = info['L'][0]
            rightArray = info['R'][0]
            frontArray = info['F'][0]
            backArray = info['B'][0]
            info[f], leftArray, backArray, rightArray, frontArray = rotate(info[f], dir, leftArray, backArray, rightArray, frontArray)
        elif f == 'F':
            upArray = info['U'][0]
            downArray = info['D'][0]
            rightArray = column(info['R'], 0)
            leftArray = column(info['L'], 0)
            info[f], upArray, temp1, downArray, temp2 = rotate(info[f], dir, upArray, leftArray, downArray, rightArray)
            info['R'] = column_input(temp2, info['R'], 0)
            info['L'] = column_input(temp1, info['L'], 0)
        elif f == 'B':
            upArray = info['U'][2]
            downArray = info['D'][2]
            rightArray = column(info['R'], 2)
            leftArray = column(info['L'], 2)
            info[f], upArray, temp1, downArray, temp2 = rotate(info[f], dir, upArray, rightArray, downArray, leftArray)
            info['R'] = column_input(temp1, info['R'], 2)
            info['L'] = column_input(temp2, info['L'], 2)
        elif f == 'L':
            upArray = column(info['U'], 0)
            downArray = column(info['D'], 0)
            frontArray = column(info['F'], 0)
            backArray = column(info['B'], 0)
            info[f], temp1, temp2, temp3, temp4 = rotate(info[f], dir, upArray, backArray, downArray, frontArray)
            info['U'] = column_input(temp1, info['U'], 0)
            info['B'] = column_input(temp2, info['B'], 0)
            info['D'] = column_input(temp3, info['D'], 0)
            info['F'] = column_input(temp4, info['F'], 0)
        elif f == 'R':
            upArray = column(info['U'], 2)
            downArray = column(info['D'], 2)
            frontArray = column(info['F'], 2)
            backArray = column(info['B'], 2)
            info[f], temp1, temp2, temp3, temp4 = rotate(info[f], dir, upArray, frontArray, downArray, backArray)
            info['U'] = column_input(temp1, info['U'], 2)
            info['F'] = column_input(temp2, info['F'], 2)
            info['B'] = column_input(temp3, info['B'], 2)
            info['D'] = column_input(temp4, info['D'], 2)

    print(info['U'])



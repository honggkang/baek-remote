from collections import deque
import copy
global N


def find_aim(pres_coord, fish_map, matrix_distance, shark_size, q4bfs, find_other):
    tx = pres_coord[0]
    ty = pres_coord[1]
    idx = 0
    for mx, my in (-1, 0), (0, -1), (0, 1), (1, 0):
        ttx = tx + mx
        tty = ty + my
        if -1 < ttx < N and -1 < tty < N and fish_map[ttx][tty] <= shark_size and matrix_distance[ttx][tty] >= matrix_distance[tx][ty]:
            if not find_other and matrix_distance[ttx][tty] == 999:
                q4bfs.append([ttx, tty])
                idx += 1
            matrix_distance[ttx][tty] = matrix_distance[tx][ty]+1
            if 0 < fish_map[ttx][tty] < shark_size:
                aim_found = True
                aim_coordinate = [ttx, tty]
                for _ in range(idx):
                    q4bfs.pop()
                return aim_found, aim_coordinate, matrix_distance, q4bfs
    aim_found = False
    aim_coordinate = [-1, -1]
    return aim_found, aim_coordinate, matrix_distance, q4bfs


N = int(input())
FishMap = [list(map(int, input().split())) for _ in range(N)]

SharkSize = 2
FishNum = 0

for _x in range(N):  # initialization
    for _y in range(N):
        if FishMap[_x][_y] != 9:
            if FishMap[_x][_y]:
                FishNum += 1
        else:
            SharkCoord = [_x, _y]
            FishMap[_x][_y] = 0

t = 0
growSize = 0
Q4BFS = deque()
Q4BFS.append(SharkCoord)
matrixDistance = [[999 for _c in range(N)] for _r in range(N)]
matrixDistance[SharkCoord[0]][SharkCoord[1]] = 0

while FishNum > 0:
    # print(SharkSize)
    # print(SharkCoord)
    if Q4BFS:  # if candidate exist
        while Q4BFS:  # until queue gets empty
            presCoord = Q4BFS.popleft()
            aimFound, aimCoord, matrixDistance, Q4BFS = find_aim(presCoord, FishMap, matrixDistance, SharkSize, Q4BFS, 0)
            if aimFound:  # aim found
                d = matrixDistance[aimCoord[0]][aimCoord[1]]
                while Q4BFS:  # check other candidates that are uppder and more left
                    presCoord = Q4BFS.popleft()
                    aimFound, tempCoord, matrixDistance, Q4BFS = find_aim(presCoord, FishMap, matrixDistance, SharkSize,
                                                                         Q4BFS, 1)
                    tempd = matrixDistance[tempCoord[0]][tempCoord[1]]
                    if aimFound and tempd == d:
                        if tempCoord[0] < aimCoord[0]:
                            aimCoord = copy.deepcopy(tempCoord)
                        elif tempCoord[0] == aimCoord[0]:
                            if tempCoord[1] < aimCoord[1]:
                                aimCoord = copy.deepcopy(tempCoord)

                solCoord = copy.deepcopy(aimCoord)
                # if solCoord[0]==0 and solCoord[1]==2:
                #     tttt=0
                solDist = matrixDistance[aimCoord[0]][aimCoord[1]]
                t = t + solDist
                SharkCoord = solCoord
                FishMap[SharkCoord[0]][SharkCoord[1]] = 0
                FishNum -= 1
                growSize += 1
                Q4BFS = deque()
                Q4BFS.append(SharkCoord)
                matrixDistance = [[999 for _c in range(N)] for _r in range(N)]
                matrixDistance[SharkCoord[0]][SharkCoord[1]] = 0
                if growSize == SharkSize:
                    growSize = 0
                    SharkSize += 1
                aimFound = False
                break
    else:
        break

    # print(minDist)

print(t)

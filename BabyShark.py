from collections import deque
global CoordBanned, N


def banned_check(x, y):
    for _ in range(len(CoordBanned)):
        if x == CoordBanned[_][0] and y == CoordBanned[_][1]:
            return True
    return False


def distance(v, w):
    Q4Path = deque()
    Q4Path.append([w[0], w[1]])
    matrix_visited = [[False for _ in range(N)] for _r in range(N)]
    matrix_visited[w[0]][w[1]] = True
    matrix_distance = [[0 for _ in range(N)] for _r in range(N)]
    di = 1
    while len(Q4Path) != 0:
        tx, ty = Q4Path.popleft()
        for mx, my in (1,0),(-1,0),(0,1),(0,-1):
            ttx = tx+mx
            tty = ty+my
            if -1 < ttx < N and -1 < tty < N and not matrix_distance[ttx][tty]:
                if not banned_check(ttx, tty):
                    Q4Path.append([ttx, tty])
                    matrix_visited[ttx][tty] = True
                    matrix_distance[ttx][tty] = matrix_distance[tx][ty]+1
                    if ttx == v[0] and tty == v[1]:
                        return matrix_distance[ttx][tty]
    return 99


def edible_banned(fish_size, shark_size):
    idx_edible = []
    idx_banned = []
    for _ in range(len(fish_size)):
        if fish_size[_] < shark_size:
            idx_edible.append(_)
        elif fish_size[_] > shark_size:
            idx_banned.append(_)
    if not idx_edible:
        idx_edible = -1
    return idx_edible, idx_banned


def find_aim(edible_idx, fish_coord, shark_coord):
    temp = []
    for _ in range(len(edible_idx)):
        temp.append(distance(fish_coord[edible_idx[_]], shark_coord))
    min_dist = min(temp)
    return edible_idx[temp.index(min_dist)], min_dist


N = int(input())
InitFishMap = [list(map(int, input().split())) for _ in range(N)]

FishSize = []
FishCoord = []  # (x-coordinate, y-coordinate)
SharkSize = 2

for _x in range(N):
    for _y in range(N):
        if InitFishMap[_x][_y] != 9:
            if InitFishMap[_x][_y]:
                FishSize.append(InitFishMap[_x][_y])
                FishCoord.append([_x, _y])
        else:
            SharkCoord = [_x, _y]

t = 0
growSize = 0

while len(FishSize) > 0:
    EdibleFishIdx, bannedPathIdx = edible_banned(FishSize, SharkSize)
    if EdibleFishIdx == -1:
        break
    CoordBanned = []
    for _ in range(len(bannedPathIdx)):
        CoordBanned.append(FishCoord[bannedPathIdx[_]])
    FishAimIdx, minDist = find_aim(EdibleFishIdx, FishCoord, SharkCoord)
    if minDist == 99:
        break
    t += minDist
    SharkCoord = FishCoord[FishAimIdx]
    print(SharkSize)
    print(SharkCoord)
    # print(minDist)
    FishCoord.pop(FishAimIdx)
    FishSize.pop(FishAimIdx)
    growSize += 1
    if growSize == SharkSize:
        growSize = 0
        SharkSize += 1

print(t)
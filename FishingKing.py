# BOJ 17143

import sys
input = sys.stdin.readline

# import time

R, C, M = map(int, input().split())
RC = [R - 1, C - 1]
sharkInput = [list(map(int, input().split())) for _ in range(M)]  # r, c, (s)peed, (d)irection, si(z)e
# start = time.time()


# d: 1 up 2 down 3 right 4 left
# pos: [r, c] = [y, x]


class Shark:
    def __init__(self, r, c, s, d, z):
        self.pos = [r - 1, c - 1]
        self.size = z
        if d == 1:
            self.dc = 0
            self.dir = [-1, 0]
        elif d == 2:
            self.dc = 0
            self.dir = [1, 0]
        elif d == 3:
            self.dc = 1
            self.dir = [0, 1]
        else:
            self.dc = 1
            self.dir = [0, -1]
        if 2*RC[self.dc]:
            self.sp = s % (2*RC[self.dc])
        else:
            self.sp = s

    def move(self):
        if self.dir[self.dc] > 0:
            v = self.sp
        else:  # self.dir[self.dc] < 0
            if self.pos[self.dc] + self.dir[self.dc] * self.sp > 0:
                v = self.sp
            else:  # moved position <= 0
                v = self.sp - self.pos[self.dc]
                self.pos[self.dc] = 0
                self.dir = [x * -1 for x in self.dir]
        rem = (self.pos[self.dc] + v * self.dir[self.dc]) % RC[self.dc]  # remainder
        if (self.pos[self.dc] + v * self.dir[self.dc]) // RC[self.dc] % 2 == 1:
            self.dir = [x * -1 for x in self.dir]
            self.pos[self.dc] = RC[self.dc] - rem
        else:
            self.pos[self.dc] = rem


gotSize = 0

if M:
    sharkSet = []
    sharkAlive = [x for x in range(M)]

    for i in range(M):
        sh = Shark(sharkInput[i][0], sharkInput[i][1], sharkInput[i][2], sharkInput[i][3], sharkInput[i][4])
        sharkSet.append(sh)

    for t in range(C):
        # sharkCandRow = []  # to-be-got shark candidate row position
        # sharkCandInd = []

        if len(sharkAlive) == 0:
            break

        kk = False
        got = False
        temp = 101
        for i in sharkAlive:
            sh = sharkSet[i]
            if sh.pos[1] == t:
                if sh.pos[0] == 0:
                    kk = True
                    sharkAlive.remove(i)
                    gotSize += sh.size
                    break
                if sh.pos[0] < temp:
                    gotcha = i
                    got = True
                    temp = sh.pos[0]
                # sharkCandRow.append(sh.pos[0])
                # sharkCandInd.append(i)

        # if not kk and sharkCandRow:
        if not kk and got:
            # gotcha = sharkCandInd[sharkCandRow.index(min(sharkCandRow))]
            sharkAlive.remove(gotcha)
            gotSize += sharkSet[gotcha].size

        # sharksPosSet = []  # position set [[r,c], [r1,c1], ... ,]
        # sharksInd = []  # index [shark1, shark3, ... ]

        sharksPosMap = [[False]*C for _ in range(R)]
        sharksPosInd = [[-1]*C for _ in range(R)]
        sharkAliveNew = sharkAlive.copy()
        for i in sharkAliveNew:
            sharkSet[i].move()
            pos = sharkSet[i].pos
            # if pos not in sharksPosSet:  # 검사 수 줄이기?
            #     sharksPosSet.append(pos)
            #     sharksInd.append(i)
            if not sharksPosMap[pos[0]][pos[1]]:
                sharksPosMap[pos[0]][pos[1]] = True
                sharksPosInd[pos[0]][pos[1]] = i
            else:
                # idx = sharksPosSet.index(pos)
                # sharkNum = sharksInd[idx]
                sharkNum = sharksPosInd[pos[0]][pos[1]]
                shc = sharkSet[sharkNum]
                if shc.size < sharkSet[i].size:  # 하나하나 비교하는것 보다 모두 모아놓고 min으로?
                    # sharkAlive.pop(sharkAlive.index(sharkNum))
                    sharkAlive.remove(sharkNum)
                    # sharksInd[idx] = i
                    sharksPosInd[pos[0]][pos[1]] = i
                else:
                    sharkAlive.remove(i)

        # print(sharksPosSet)

print(gotSize)

# print("time :", time.time() - start)
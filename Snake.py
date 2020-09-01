# BOJ 3190
import sys


class Snake:
    def __init__(self):
        self.headPos = [0, 0]
        self.body = []
        self.direction = 'r'

    def move(self, prev):
        self.body.insert(0, prev)
        if self.direction == 'r':  # right
            self.headPos[1] += 1
        elif self.direction == 'l':  # left
            self.headPos[1] -= 1
        elif self.direction == 'u':  # up
            self.headPos[0] -= 1
        else:  # down
            self.headPos[0] += 1
        return self.headPos

    def no_apple(self):
        self.body.pop()  # pop(): last array


input = sys.stdin.readline

N = int(input())  # of map size
K = int(input())  # of apple
appleMap = [list(map(int, input().split())) for _ in range(K)]
for _ in range(len(appleMap)):
    appleMap[_][0] -= 1
    appleMap[_][1] -= 1

L = int(input())  # of snake direction variation
snakeMob = [list(input().split()) for _ in range(L)]
# L: left, D: right, N: neutral

baam = Snake()
t = 0
fl = False

for i in range(L):
    if i == 0:
        tt = int(snakeMob[i][0])
    else:
        tt = int(snakeMob[i][0]) - int(snakeMob[i-1][0])
    for _ in range(tt):
        snakeHead = baam.headPos.copy()
        baam.move(snakeHead)
        print(baam.headPos)
        if baam.headPos in baam.body:
            fl = True
            break
        elif baam.headPos[0] >= N or baam.headPos[0] < 0 or baam.headPos[1] >= N or baam.headPos[1] < 0:
            fl = True
            break
        if baam.headPos in appleMap:
            appleMap.remove(baam.headPos)
        else:
            baam.no_apple()
        t += 1

    if fl:
        break

    if baam.direction == 'r':
        if snakeMob[i][1] == 'L':
            baam.direction = 'u'
        else:
            baam.direction = 'd'
    elif baam.direction == 'l':
        if snakeMob[i][1] == 'L':
            baam.direction = 'd'
        else:
            baam.direction = 'u'
    elif baam.direction == 'u':
        if snakeMob[i][1] == 'L':
            baam.direction = 'l'
        else:
            baam.direction = 'r'
    elif baam.direction == 'd':
        if snakeMob[i][1] == 'L':
            baam.direction = 'r'
        else:
            baam.direction = 'l'

while not fl:
    snakeHead = baam.headPos.copy()
    baam.move(snakeHead)
    print(baam.headPos)
    if baam.headPos in baam.body:
        fl = True
        break
    elif baam.headPos[0] >= N or baam.headPos[0] < 0 or baam.headPos[1] >= N or baam.headPos[1] < 0:
        fl = True
        break
    if baam.headPos in appleMap:
        appleMap.remove(baam.headPos)
    else:
        baam.no_apple()
    t += 1

print(t+1)
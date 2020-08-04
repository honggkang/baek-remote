global Weight, Value, N, K, temp, bagItem, sortedIdx
Weight = []; Value = []; CostEffect = []

N, K = map(int, input().split())
WeightValue = [list(map(int, input().split())) for _ in range(N)]

# N = 6
# K = 9
# WeightValue = [[3, 6], [2, 7], [4, 6], [4, 2], [4, 10], [1, 5]]

# N = 10
# K = 10
# WeightValue = [[1, 2], [4, 9], [1, 5], [4, 8], [4, 1], [1, 7], [3, 2], [3, 7], [2, 5], [5, 2]]

# N = 5
# K = 9
# WeightValue = [[2, 4], [1, 3], [3, 5], [4, 8], [2, 1]]

# N = 4
# K = 5
# WeightValue = [[1, 4], [1, 8], [3, 3], [4, 8]]

for _ in range(N):
    Weight.extend([WeightValue[_][0]])
    Value.extend([WeightValue[_][1]])
    CostEffect.extend([WeightValue[_][1] / WeightValue[_][0]])

# N = 4
# K = 7
# Weight = [6, 4, 3, 5]
# Value = [13, 8, 6, 12]
# CostEffect = [2.1666666666666665, 2.0, 2.0, 2.4]

# CostEffect.sort()
# [i[0] for i in sorted(enumerate(CostEffect), key=lambda x:x[1])]
sortedIdx = sorted(range(len(CostEffect)), key=CostEffect.__getitem__, reverse=True)

temp = 0
bagItem = []
bag = [0, 0]

# failure of greedy algorithm
def sequential_combination(idx):
    global temp
    myiter = iter(range(idx, N))
    for ii in myiter:
        i = sortedIdx[ii]
        end_flag = False
        if bag[0]+Weight[i] <= K:
            if i == 4:
                flag = True
            put(Weight[i], Value[i])
            bagItem.append(i)
            flag = True # item has been put
            temp = max(temp, bag[1])
            if len(bagItem) == N:
                end_flag = True
                return end_flag # output index
            else:
                if ii != N-1:
                    ii += 1
                    end_flag = sequential_combination(ii)
            if len(bagItem) == 0:
                end_flag = True
                return end_flag
            else:
                t = bagItem.pop()
                put(-Weight[t], -Value[t])

        if end_flag:
            return end_flag


def put(weight, value):
    bag[0] += weight
    bag[1] += value


sequential_combination(0)
print(temp)
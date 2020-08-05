import copy as cp

global N
# N, K = map(int, input().split())
# itemsList = [list(map(int, input().split())) for _ in range(N)]  # weight, value

N = 6
K = 9
itemsWeightValue = [[3, 6], [2, 7], [4, 6], [4, 2], [4, 10], [1, 5]]

# N = 4
# K = 5
# itemsWeightValue = [[1, 4], [1, 8], [3, 3], [4, 8]]

# N = 10
# K = 10
# itemsWeightValue = [[1, 2], [4, 9], [1, 5], [4, 8], [4, 1], [1, 7], [3, 2], [3, 7], [2, 5], [5, 2]]

# N = 5
# K = 9
# itemsWeightValue = [[2, 4], [1, 3], [3, 5], [4, 8], [2, 1]]

# N = 4
# K = 7
# Weight = [6, 4, 3, 5]
# Value = [13, 8, 6, 12]
# CostEffect = [2.1666666666666665, 2.0, 2.0, 2.4]

# CostEffect.extend([items[_][1] / items[_][0]])

# CostEffect.sort()
# [i[0] for i in sorted(enumerate(CostEffect), key=lambda x:x[1])]

# sortedIdx = sorted(range(len(CostEffect)), key=CostEffect.__getitem__, reverse=True)


def init(items_weight_value):
    items_weight_value.sort()
    items_weight = [];
    items_value = []
    for _ in range(N):
        items_weight.extend([items_weight_value[_][0]])
        items_value.extend([items_weight_value[_][1]])
    min_weight = items_weight[0]
    max_weight = items_weight[N-1]
    min_item_num = items_weight.count(min_weight)
    min_idx = items_weight.index(min_weight)
    min_weight_item_max_value = max(items_value[min_idx:min_idx + min_item_num])

    pick_item_idx = items_weight_value.index([min_weight, min_weight_item_max_value])
    value_map = [0 for _ in range(K+1)]
    value_map[min_weight] = min_weight_item_max_value
    return items_weight, items_value, pick_item_idx, value_map, min_weight, max_weight


def fill_in(weight_idx, available_items_indices, value_map, items_weight, items_weight_value):
    for w in items_weight:
        copied_indices = cp.deepcopy(available_items_indices)
        if weight_idx - w > 0:
            available_items_weight_value = []
            for _ in available_items_indices[weight_idx - w]:
                available_items_weight_value.append(items_weight_value[_])
            available_items_weight = []
            available_items_value = []
            for _ in range(len(available_items_weight_value)):
                available_items_weight.extend([available_items_weight_value[_][0]])
                available_items_value.extend([available_items_weight_value[_][1]])

            if w in available_items_weight:
                item_num = available_items_weight.count(w)
                if item_num > 0:
                    item_idx = available_items_weight.index(w)
                    v = max(available_items_value[item_idx:item_idx + item_num])
                    pick_item_idx = available_items_weight_value.index([w, v])

                if value_map[weight_idx] == 0:
                    if value_map[weight_idx-w] + v > value_map[weight_idx-1]:
                        copied_indices[weight_idx - w].pop(pick_item_idx)
                        available_items_indices[weight_idx] = copied_indices[weight_idx - w]
                        value_map[weight_idx] = value_map[weight_idx - w] + v
                    else:
                        available_items_indices[weight_idx] = copied_indices[weight_idx - 1]
                        value_map[weight_idx] = value_map[weight_idx - 1]
                else:
                    if value_map[weight_idx] < value_map[weight_idx-w] + v:
                        copied_indices[weight_idx - w].pop(pick_item_idx)
                        available_items_indices[weight_idx] = copied_indices[weight_idx - w] # temporary variable required
                        value_map[weight_idx] = value_map[weight_idx-w] + v
            else:
                available_items_indices[weight_idx] = copied_indices[weight_idx - 1]
                value_map[weight_idx] = value_map[weight_idx - 1]


    return available_items_indices, value_map


itemsWeight, itemsValue, pickIdx, valueMap, minWeight, maxWeight = init(itemsWeightValue)
AvailableItemsIndices = [[i for i in range(N)] for _ in range(K+1)]
for _ in range(minWeight):
    AvailableItemsIndices[_] = []
AvailableItemsIndices[minWeight].pop(pickIdx)

itemsWeightNoOverlap = list(set(itemsWeight))
for _ in range(minWeight+1, K+1):
    AvailableItemsIndices, valueMap = fill_in(_, AvailableItemsIndices, valueMap, itemsWeightNoOverlap, itemsWeightValue)

print(valueMap[len(valueMap)-1])
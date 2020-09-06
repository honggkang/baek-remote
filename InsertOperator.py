# BOJ 14888

import sys
global nums
max_res = -1e9
min_res = 1e9

input = sys.stdin.readline

N = int(input())
nums = list(map(int, (input().split())))
operatorList = list(map(int, input().split()))  # plus, minus, times, divide
# operatorList = [p, m, t, d]

# DFS
def DFS(pre_num, depth, operator_list):
    global max_res, min_res
    if sum(operator_list) > 0:
        depth += 1
        for oi in range(4):
            if oi == 0 and operator_list[0] > 0:
                num = pre_num + nums[depth]
                operator_list[oi] -= 1
                DFS(num, depth, operator_list)
                operator_list[oi] += 1
            elif oi == 1 and operator_list[1] > 0:
                num = pre_num - nums[depth]
                operator_list[oi] -= 1
                DFS(num, depth, operator_list)
                operator_list[oi] += 1
            elif oi == 2 and operator_list[2] > 0:
                num = pre_num * nums[depth]
                operator_list[oi] -= 1
                DFS(num, depth, operator_list)
                operator_list[oi] += 1
            elif oi == 3 and operator_list[3] > 0:
                if pre_num < 0:
                    temp = -pre_num // nums[depth]
                    num = -temp
                else:
                    num = pre_num // nums[depth]
                operator_list[oi] -= 1
                DFS(num, depth, operator_list)
                operator_list[oi] += 1
    else: #  the deepest
        max_res = max(max_res, pre_num)
        min_res = min(min_res, pre_num)



depth = 0
DFS(nums[0], depth, operatorList)
print(max_res)
print(min_res)
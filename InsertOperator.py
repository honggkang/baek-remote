# BOJ 14888

import sys
global nums
    # , max_res, min_res
max_res = -1e9
min_res = 1e9

input = sys.stdin.readline

N = int(input())
nums = list(map(int, (input().split())))
operatorList = list(map(int, input().split()))  # plus, minus, times, divide
# operatorList = [p, m, t, d]


# def insert_operator(pre_num, post_num, operator_list):
#     if operator_list[0] > 0:
#         num = pre_num + post_num
#         operator_list[0] -= 1
#     elif operator_list[1] > 0:
#         num = pre_num - post_num
#         operator_list[1] -= 1
#     elif operator_list[2] > 0:
#         num = pre_num * post_num
#         operator_list[2] -= 1
#     elif operator_list[3] > 0:
#         if pre_num < 0:
#             temp = -pre_num//post_num
#             num = -temp
#         else:
#             num = pre_num//post_num
#     return num, operator_list


# DFS
def DFS(pre_num, depth, operator_list):
    global max_res, min_res
    if sum(operator_list) > 0:
        operator_list_temp = operator_list.copy()
        depth += 1
        for oi in range(4):
            if oi == 0 and operator_list[0] > 0:
                num = pre_num + nums[depth]
                operator_list_temp[0] -= 1
                DFS(num, depth, operator_list_temp)
                operator_list_temp[0] += 1
            elif oi == 1 and operator_list[1] > 0:
                num = pre_num - nums[depth]
                operator_list_temp[1] -= 1
                DFS(num, depth, operator_list_temp)
                operator_list_temp[1] += 1
            elif oi == 2 and operator_list[2] > 0:
                num = pre_num * nums[depth]
                operator_list_temp[2] -= 1
                DFS(num, depth, operator_list_temp)
                operator_list_temp[2] += 1
            elif oi == 3 and operator_list[3] > 0:
                if pre_num < 0:
                    temp = -pre_num // nums[depth]
                    num = -temp
                else:
                    num = pre_num // nums[depth]
                operator_list_temp[3] -= 1
                DFS(num, depth, operator_list_temp)
                operator_list_temp[3] += 1
    else: #  the deepest
        max_res = max(max_res, pre_num)
        min_res = min(min_res, pre_num)



depth = 0
DFS(nums[0], depth, operatorList)
print(max_res)
print(min_res)
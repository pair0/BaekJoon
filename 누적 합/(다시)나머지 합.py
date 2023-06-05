### 시간 초과
# import sys
# from itertools import combinations
# input = sys.stdin.readline

# N, M = map(int, input().split())
# N_list = list(map(int, input().split()))
# sum_list = [0]
# total = 0
# answer = 0

# for i in range(N):
#     total += N_list[i]
#     sum_list.append(total)

# for i in combinations(sum_list, 2):
#     if (i[1] - i[0]) % M == 0:
#         answer += 1

# print(answer)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
numRemainder = [0] * M
total = 0

for i in range(N):
    total += N_list[i]
    numRemainder[total % M] += 1 ### 나머지 같은 것의 갯수 세기

answer = numRemainder[0]
print(numRemainder)

for i in numRemainder:
    answer += i*(i-1)//2 ### 나머지가 같은 것끼리 조합

print(answer)


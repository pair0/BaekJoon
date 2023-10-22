# ## 시간초과 (그냥 구현)
# import sys
# from collections import Counter
# input = sys.stdin.readline

# N, H = map(int, input().split()) ### N은 항상 짝수
# down_size = list()
# up_size = list()
# answer_list = list()

# for i in range(N//2):
#     down_size.append(int(input()))
#     up_size.append(int(input()))

# for i in range(1, H+1):
#     answer = 0
#     for j in range(N//2):
#         if i <= down_size[j]:
#             answer += 1
#         if i > H-up_size[j]:
#             answer += 1
#     answer_list.append(answer)

# # print(down_size, up_size)
# result = sorted(list(Counter(answer_list).most_common()))
# print(result[0][0], result[0][1])

### 다른 풀이 (이진 분류)
import sys
from bisect import bisect_left, insort, bisect

input = sys.stdin.readline

N, H = map(int, input().split())  ### N은 항상 짝수
down_size = list()
up_size = list()
answer_list = list()
min_value = N + 1
answer = 0

for i in range(N // 2):
    down_size.append(int(input()))  ### 종유석
    up_size.append(H - int(input()))  ### 석순

down_size.sort()
up_size.sort()
print(up_size)

for i in range(1, H + 1):
    total = (N // 2 - bisect_left(down_size, i)) + bisect_left(up_size, i)
    answer_list.append(total)

answer_list.sort()

for i in answer_list:
    if min_value >= i:
        min_value = i
        answer += 1
    else:
        break

print(answer_list[0], answer)

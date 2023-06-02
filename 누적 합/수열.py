import sys
input = sys.stdin.readline

N, K = map(int, input().split())
N_list = list(map(int, input().split()))
sum_list = [0]
total = 0
max_answer = 0
flag = 0

for i in range(N):
    total += N_list[i]
    sum_list.append(total)

for i in range(N, K-1, -1):
    value = sum_list[i] - sum_list[i-K]
    if max_answer < value or flag == 0:
        max_answer = value
        flag = 1

print(max_answer)
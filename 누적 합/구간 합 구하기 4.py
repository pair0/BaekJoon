import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list(map(int, input().split()))
sum_list = [0]
answer = 0

for i in range(N):
    answer += N_list[i]
    sum_list.append(answer)

for _ in range(M):
    i, j = map(int, input().split())
    print(sum_list[j] - sum_list[i - 1])
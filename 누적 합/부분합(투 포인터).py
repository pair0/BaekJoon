import sys
input = sys.stdin.readline

N, S = map(int, input().split())
N_list = list(map(int, input().split()))
sum_list = [0]
start, end = 1, 1
total = 0
min_len = N+2

for i in range(N):
    total += N_list[i]
    sum_list.append(total)

if sum_list[N] < S:
    print(0)
    exit()

while start <= end and end <= N:
    total = sum_list[end] - sum_list[start-1]

    if total >= S:
        value = end - start
        if min_len > value:
            min_len = value
        start += 1
    else:
        end += 1
        
print(min_len+1)
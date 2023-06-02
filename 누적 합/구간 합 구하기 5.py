import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = list()
sum_list = [[0] * (N+1)]

for i in range(N):
    N_list.append(list(map(int, input().split())))

for i in range(N):
    answer = 0
    sum_list.append([0])
    for j in range(N):
        answer += N_list[i][j]
        sum_list[i+1].append(answer)

for i in range(1, N+1): ### x값
    for j in range(1, N+1): ### y값
        sum_list[j][i] +=  sum_list[j-1][i]

for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(sum_list[x2][y2] - (sum_list[x1-1][y2] + sum_list[x2][y1-1]) + sum_list[x1-1][y1-1])

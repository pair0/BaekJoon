import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
answer = [0] * M

N_list.sort()

for i in range(M):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        
        if N_list[mid] < M_list[i]:
            start = mid + 1
        elif N_list[mid] > M_list[i]:
            end = mid - 1
        else:
            answer[i] = 1
            break

print(*answer)
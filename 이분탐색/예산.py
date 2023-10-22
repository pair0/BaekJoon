import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())

if M >= sum(N_list):
    print(max(N_list))
else:
    N_list.sort()
    start, end = 0, max(N_list)
    while start <= end:
        mid = (start+end) // 2
        total = 0
        for i in N_list:
            if i > mid:
                total += mid
            else:
                total += i
        if total > M:
            end = mid - 1
        else:
            start = mid + 1
    print(end)
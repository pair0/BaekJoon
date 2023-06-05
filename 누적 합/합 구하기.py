import sys
input = sys.stdin.readline

N = int(input())
Aarr = list(map(int, input().split()))
M = int(input())
total = 0
Asum = [0]

for i in range(N):
    total += Aarr[i]
    Asum.append(total)

for _ in range(M):
    i, j = map(int, input().split())
    print(Asum[j] - Asum[i-1])
import sys
input = sys.stdin.readline

n = int(input())
lst = [0] + list(map(int, input().split()))
k = int(input())
dp = [[0 for _ in range(n+1)] for _ in range(4)]
for i in range(1, 4):
    for j in range(k*i, n+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j-k] + sum(lst[j-k+1:j+1]))

print(dp[3][n])
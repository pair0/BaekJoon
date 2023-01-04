import sys

dp = [0, 1]


def fibo(n):
    while len(dp) < n+1:
        dp.append(dp[len(dp)-1]+dp[len(dp)-2])

n = int(sys.stdin.readline())
fibo(n)
print(dp[n])
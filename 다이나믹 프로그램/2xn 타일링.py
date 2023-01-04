import sys

dp = [1, 2] ## 초기 2x1, 2x2의 값을 넣어준다.


def sqare(n):
    while len(dp) < n:
        dp.append(dp[len(dp)-1]+dp[len(dp)-2])


n = int(sys.stdin.readline())
sqare(n)
print(dp[n-1]%10007)
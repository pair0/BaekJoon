import sys

T = int(sys.stdin.readline())


for i in range(T):
    k = int(sys.stdin.readline()) ## 층
    n = int(sys.stdin.readline()) ## 호
    dp = [x for x in range(1, n+1)] ## 0층 리스트

    for j in range(k): ## 해당 층 수 만큼 반복
        for l in range(1, n): ## 1~ n-1까지
            dp[l] += dp[l-1] ## 층별 각 호실의 사람 수를 변경
    print(dp[-1])

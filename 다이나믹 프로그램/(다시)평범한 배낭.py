import sys

def knapsack(N, K, items):
    # dp[i][w]는 i번째 물건까지 고려하고 배낭의 무게가 w일 때의 최대 가치를 나타냅니다.
    dp = [[0] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for w in range(1, K + 1):
            weight, value = items[i - 1]
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    return dp[N][K]

if __name__ == "__main__":
    N, K = map(int, input().split())
    items = []

    for i in range(N):
        weight, value = map(int, input().split())
        items.append((weight, value))

    result = knapsack(N, K, items)
    print(result)

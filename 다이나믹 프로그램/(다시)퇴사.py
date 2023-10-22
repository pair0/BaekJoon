import sys

input = sys.stdin.readline


def solution(N, graph):
    dp = [0 for i in range(N + 1)]

    for i in range(N):
        for j in range(i + graph[i][0], N + 1):
            if dp[j] < dp[i] + graph[i][1]:
                dp[j] = dp[i] + graph[i][1]

    print(dp[-1])


if __name__ == "__main__":
    N = int(input())
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    solution(N, graph)

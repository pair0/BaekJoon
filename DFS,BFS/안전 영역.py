import sys
from collections import deque


def bfs(graph, x, y, rain):
    queue = deque([(x, y)])
    visited[y][x] = True

    # 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and graph[ny][nx] > rain:
                queue.append((nx, ny))
                visited[ny][nx] = True


if __name__ == "__main__":
    N = int(sys.stdin.readline())

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    max_value = 0

    for i in range(max(sum(graph, []))):
        answer = 0
        visited = [[False] * N for _ in range(N)]
        for j in range(N):
            for k in range(N):
                if graph[j][k] > i and not visited[j][k]:
                    bfs(graph, k, j, i)
                    answer += 1

        if max_value < answer:
            max_value = answer

    print(max_value)

import sys
from collections import deque


def bfs(graph_map, x, y):
    queue = deque([(x, y)])
    visited[y][x] = True

    # 상하좌우대각선 정의
    dx = [0, 0, -1, 1, 1, -1, 1, -1]
    dy = [-1, 1, 0, 0, -1, 1, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and graph_map[ny][nx] != 0:
                queue.append((nx, ny))
                visited[ny][nx] = True


while True:
    w, h = map(int, sys.stdin.readline().split())

    if w == 0 and h == 0:
        break

    graph_map = [list(map(int, sys.stdin.readline().split()))
                 for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    answer = 0

    for i in range(h):
        for j in range(w):
            if graph_map[i][j] == 1 and not visited[i][j]:
                bfs(graph_map, j, i)
                answer += 1

    print(answer)

import sys
from collections import deque

input = sys.stdin.readline

def solution(N, M, x, y, graph):
    visited = [[0]*M for _ in range(N)]
    queue = deque([(x, y)])
    visited[y][x] = 1

    #상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == 0 and graph[ny][nx] != "W":
                queue.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1

    return visited[y][x] - 1

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = []
    max_va = -1
    for i in range(N):
        graph.append(list(input()))
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "L":
                answer = solution(N, M, j, i, graph)

                if max_va < answer:
                    max_va = answer
    print(max_va)
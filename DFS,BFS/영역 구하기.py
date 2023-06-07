import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, x, y):
    count = 1
    queue = deque([(x, y)])
    graph[y][x] = 1

    ### 방향 정의
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0:
                queue.append((nx, ny))
                graph[ny][nx] = 1
                count += 1
    return count

if __name__== "__main__":
    M, N, K = map(int, input().split())
    graph = [[0] * N for _ in range(M)]
    answer = 0
    answer_list = list()

    for i in range(K):
        x, y, x1, y1 = map(int, input().split())
        for j in range(y, y1):
            graph[j][x: x1] = [-1] * (x1 - x)
    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 0:
                answer_list.append(bfs(graph, j, i))
                answer += 1

    print(answer)
    print(*sorted(answer_list))
import sys
from collections import deque

def bfs(graph, x, y, flag):
    queue = deque([(x, y)])
    if flag == 0:
        visited[y][x] = True
    else:
        visited_red[y][x] = True

    ### 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == graph[y][x] and not visited[ny][nx] and flag == 0:
                queue.append((nx, ny))
                visited[ny][nx] = True
            
            if 0 <= nx < N and 0 <= ny < N and graph[ny][nx] == graph[y][x] and not visited_red[ny][nx] and flag == 1:
                queue.append((nx, ny))
                visited_red[ny][nx] = True



if __name__ == "__main__":
    N = int(sys.stdin.readline())
    graph = list()
    graph_red = list()
    for i in range(N):
        s = sys.stdin.readline().strip()
        graph.append(list(s))
        graph_red.append(list(s.replace("G", "R")))

    visited = [[False] * N for _ in range(N)]
    visited_red = [[False] * N for _ in range(N)]
    answer = [0, 0]
    
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(graph, j, i, 0)
                answer[0] += 1
            if not visited_red[i][j]:
                bfs(graph_red, j, i, 1)
                answer[1] += 1

    print(*answer)
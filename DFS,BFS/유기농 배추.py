import sys
from collections import deque

def bfs(list_map, x, y):
    queue = deque([(x, y)])
    list_map[y][x] = 2

    ### 상하좌우 표시
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= M or nx < 0 or ny >= N or ny < 0 or list_map[ny][nx] != 1:
                continue
            else:
                queue.append((nx, ny))
                list_map[ny][nx] = 2



T = int(sys.stdin.readline())

for test_case in range(1, T+1):
    M, N, K = map(int, sys.stdin.readline().split())
    list_map = [[0]*M for _ in range(N)]
    answer = 0

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        list_map[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if list_map[i][j] == 1:
                bfs(list_map, j, i)
                answer += 1

    print(answer)

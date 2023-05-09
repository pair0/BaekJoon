import sys
from collections import deque


M, N, H = map(int, sys.stdin.readline().split())
answer = 0
graph = list()
queue = deque()

for k in range(H):
    graph.append(list())
    for i in range(N):
        graph[k].append(list(map(int, sys.stdin.readline().split())))
        for j in range(M): #익은 토마토 큐에 저장
            if graph[k][i][j]==1:
                queue.append((j, i, k))

### 상하좌우위아래 정의
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while queue:
    x, y, z = queue.popleft()

    for i in range(6):

        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        
        if 0 <= nx < M and 0 <= ny < N and 0 <= nz < H and graph[nz][ny][nx] == 0:
            queue.append((nx, ny, nz))
            graph[nz][ny][nx] = graph[z][y][x] + 1
            
for k in graph:
    for i in k:
        for j in i:
            if j==0:
                print(-1)
                exit(0)
        answer = max(answer, max(i))

print(answer - 1)
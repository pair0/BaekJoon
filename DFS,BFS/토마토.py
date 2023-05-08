import sys
from collections import deque


M, N = map(int, sys.stdin.readline().split())
answer = 0
graph = list()
queue = deque()

for i in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

    for j in range(M): #익은 토마토 큐에 저장
        if graph[i][j]==1:
            queue.append((j, i))
    
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

while queue:
    x, y = queue.popleft()

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N and graph[ny][nx] == 0:
            queue.append((nx, ny))
            graph[ny][nx] = graph[y][x] + 1
            
for i in graph:
    for j in i:
        if j==0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)
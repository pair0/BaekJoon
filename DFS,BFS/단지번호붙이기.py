import sys
from collections import deque

N = int(sys.stdin.readline())
graph = [[] * N for _ in range(N)]
visited = [[False] * N for _ in range(N)]
answer = []


def bfs(x, y):
    count = 1
    # 상하좌우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    # 방문 할 것
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        # 현재 위치 (방문 처리)
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖으로 나가면 안됨
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue

            # 벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            # 벽이 아니므로 이동
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                # 이동한 횟수 세기
                queue.append((nx, ny))
                visited[nx][ny] = True
                count += 1

    return count


for index in range(N):
    n = sys.stdin.readline().strip()
    for k in n:
        graph[index].append(int(k))

for h in range(N):
    for w in range(N):
        if graph[h][w] == 1 and not visited[h][w]:
            answer.append(bfs(h, w))

print(len(answer))
for p in sorted(answer):
    print(p)

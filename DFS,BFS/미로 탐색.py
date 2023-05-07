from collections import deque
import sys

def bfs(graph, x, y):
    #상하좌우 정의
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    #방문 할 것
    queue.append((x,y))
    while queue:
        #현재 위치 (방문 처리)
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 밖으로 나가면 안됨
            if nx < 0 or ny < 0 or nx>=N or ny>=M:
                continue

            #벽이므로 진행 불가
            if graph[nx][ny] == 0:
                continue

            #벽이 아니므로 이동
            if graph[nx][ny] == 1:
                #이동한 횟수 세기
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[N - 1][M - 1]


N, M = map(int, sys.stdin.readline().split(" "))

##필요에 따라 방문 유무 확인 행렬 생성
# visited = [[False] * M for _ in range(N)]
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().rstrip())))

print(bfs(graph, 0, 0))
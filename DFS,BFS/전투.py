import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split(" "))

graph = []
visited = [[False] * N for _ in range(M)]

for _ in range(M):
    graph.append(list(sys.stdin.readline().rstrip()))

def bfs(y, x, color):
    count = 1
    #상하좌우 표시
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    queue = deque()
    # 방문할 것 표시
    queue.append((y,x))
    visited[y][x] = True

    #방문할 것이 없으면 반복문 종료
    while queue:
        #방문한 것
        y, x = queue.popleft()


        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or ny<0 or nx>=N or ny>=M:
                continue
            if not visited[ny][nx] and graph[ny][nx] == color:
                queue.append((ny,nx))
                visited[ny][nx] = True
                count += 1
    return count

white, blue = 0, 0

for i in range(M):
    for j in range(N):
        if graph[i][j] == 'W' and not visited[i][j]:
            white += bfs(i, j, 'W') ** 2
        elif graph[i][j] == 'B' and not visited[i][j]:
            blue += bfs(i, j, 'B') ** 2

print(white, blue)

# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
#
# def bfs(x, y, color):
#     cnt = 0
#     queue = deque()
#     queue.append((x, y))
#     visited[x][y] = True
#
#     while queue:
#         print(queue)
#         x, y = queue.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < m and 0 <= ny < n:
#                 if graph[nx][ny] == color and not visited[nx][ny]:  # each color check
#                     visited[nx][ny] = True
#                     queue.append((nx, ny))
#                     cnt += 1  # each color count
#
#     return cnt + 1
#
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
# n, m = map(int, input().split())
# graph = [list(input()) for _ in range(m)]
# visited = [[False] * n for i in range(m)]
#
# white, blue = 0, 0
# for i in range(m):
#     for j in range(n):
#         if graph[i][j] == 'W' and not visited[i][j]:
#             white += bfs(i, j, 'W') ** 2  # count accumulate
#         elif graph[i][j] == 'B' and not visited[i][j]:
#             blue += bfs(i, j, 'B') ** 2  # count accumulate
#
# print(white, blue)
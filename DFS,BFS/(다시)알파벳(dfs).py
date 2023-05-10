# import sys
# from collections import deque


# def bfs(graph, x, y, visited=deque()):
#     global answer
#     queue = deque([(x, y)])
#     visited.append(graph[y][x])

#     # 상하좌우 정의
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]

#     while queue:
#         x, y = queue.popleft()

#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]

#             if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] not in visited:
#                 queue.append((nx, ny))
#                 visited.append(graph[ny][nx])
#                 answer += 1


# def dfs(graph, x, y, answer):
#     queue = deque([(x, y)])
#     visited.append(graph[y][x])
#     print(visited)

#     x, y = queue.popleft()

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]

#         if 0 <= nx < C and 0 <= ny < R and graph[ny][nx] not in visited:
#             dfs(graph, nx, ny, answer + 1)
#             visited = deque()
#             visited.append(graph[ny][nx])


# if __name__ == "__main__":
#     R, C = map(int, sys.stdin.readline().split())
#     answer = 1
#     visited = deque()

#     # 상하좌우 정의
#     dx = [0, 0, -1, 1]
#     dy = [-1, 1, 0, 0]

#     graph = [list(sys.stdin.readline().strip()) for _ in range(R)]

#     dfs(graph, 0, 0, answer)

#     print(answer)


import sys
from collections import deque
input = sys.stdin.readline


def dfs(x, y, cnt):
    global maxi
    maxi = max(cnt, maxi)
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < R and 0 <= ny < C and check[ord(arr[nx][ny])-65] == 0:
            check[ord(arr[nx][ny])-65] = 1
            ncnt = cnt+1
            dfs(nx, ny, ncnt)
            check[ord(arr[nx][ny])-65] = 0


if __name__ == "__main__":
    R, C = map(int, input().split())
    arr = [list(input()) for _ in range(R)]
    check = [0]*(26)

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    maxi = 0

    check[ord(arr[0][0])-65] = 1
    dfs(0, 0, 1)

    print(maxi)

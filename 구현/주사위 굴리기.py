import sys

input = sys.stdin.readline

N, M, X, Y, K = map(int, input().split())
graph = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dice = [0, 0, 0, 0, 0, 0]

def turn(dir):
    a, b, c, d, e, f = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]
    if dir == 1: #동
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = d, b, a, f, e, c

    elif dir == 2: #서
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = c, b, f, a, e, d

    elif dir == 3: #북
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = e, a, c, d, f, b

    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = b, f, c, d, a, e

for _ in range(N):
    graph.append(list(map(int, input().split())))

comm = list(map(int, input().split()))

nx, ny = X, Y
for i in comm:
    nx += dx[i-1]
    ny += dy[i-1]

    if nx< 0 or nx >= N or ny < 0 or ny >= M:
        nx -= dx[i-1]
        ny -= dy[i-1]
        continue
    turn(i)
    if graph[nx][ny] == 0:
        graph[nx][ny] = dice[-1]
    else:
        dice[-1] = graph[nx][ny]
        graph[nx][ny] = 0

    print(dice[0])
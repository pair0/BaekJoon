### 시간초과
import sys
from collections import deque
import copy


def bfs():
    queue = deque()

    ### 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    ### 2위치를 전부 queue에 append
    graph_copy = copy.deepcopy(graph)
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 2:
                queue.append((j, i))
    
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N:
                if graph_copy[ny][nx] == 0:
                    graph_copy[ny][nx] = 2
                    queue.append((nx, ny))
    
    global answer
    count = 0
    for i in range(N):
        for j in range(M):
            if graph_copy[i][j] == 0:
                count += 1

    answer = max(answer, count)


def make_wall(count):
    if count == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(count+1)
                graph[i][j] = 0


N, M = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

answer = 0
make_wall(0)

print(answer)


import sys; input = sys.stdin.readline
import copy
from itertools import combinations

def solve():
    global answer
    # 새롭게 세울 벽 3개의 모든 조합 얻기
    for wall_combi in combinations(empty, wall_num):
        # 기존 맵 정보 깊은 복사(Deep Copy)
        graph_copy = copy.deepcopy(graph)
        for x_w, y_w in wall_combi:
            graph_copy[x_w][y_w] = 1
        # 바이러스 위치
        virus = [(n, m) for n in range(N) for m in range(M) if graph_copy[n][m] == 2]
        # 바이러스마다 전파 끝날 때까지 반복
        while virus:
            x_v, y_v = virus.pop()
            for dx, dy in direction:
                nx = x_v + dx
                ny = y_v + dy
                if 0 <= nx < N and 0 <= ny < M and graph_copy[nx][ny] == 0:
                    graph_copy[nx][ny] = 2
                    virus.append((nx, ny)) # 바이러스 전파
        # 안전지대 개수 카운팅
        safezone_cnt = 0
        for row in graph_copy:
            safezone_cnt += row.count(0)
        answer = max(answer, safezone_cnt)

if __name__ == "__main__":
    N, M = map(int, input().split())
    wall_num = 3
    graph = [list(map(int, input().split())) for _ in range(N)]
    # 벽을 세울 수 있는 빈 공간 정보를 리스트에 저장
    empty = [(n, m) for n in range(N) for m in range(M) if graph[n][m] == 0]
    direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    answer = 0
    solve()
    print(answer)

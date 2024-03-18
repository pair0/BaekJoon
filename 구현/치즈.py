import sys

input = sys.stdin.readline
from collections import deque
from copy import deepcopy

# 상하좌우 정의
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs_init(y, x, mapList, visited, N, M):
    queue = deque([(x, y)])
    visited[y][x] = True
    mapList[y][x] = -1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (
                0 <= nx < M
                and 0 <= ny < N
                and mapList[ny][nx] != 1
                and not visited[ny][nx]
            ):
                queue.append((nx, ny))
                visited[ny][nx] = True
                mapList[ny][nx] = -1


def solution(N, M, mapList):
    answer = 0
    last_ci = 0

    # 초기 공기 표시
    visited = [[False] * M for _ in range(N)]
    bfs_init(0, 0, mapList, visited, N, M)

    while True:
        if answer > 0:
            for i in range(N):
                for j in range(M):
                    if mapList[i][j] == 0:
                        for k in range(4):
                            nx = j + dx[k]
                            ny = i + dy[k]

                            if mapList[ny][nx] == -1:
                                bfs_init(i, j, mapList, visited, N, M)
                                break

        popList = list()
        for i in range(N):
            for j in range(M):
                if mapList[i][j] == 1:
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]

                        if mapList[ny][nx] == -1:
                            popList.append((j, i))
                            visited[i][j] = True
                            break
        copyList = deepcopy(mapList)

        for p in popList:
            mapList[p[1]][p[0]] = -1

        answer += 1

        total = 0
        for i in range(N):
            total += mapList[i].count(1)
            # print(mapList[i].count(1))

        if total == 0:
            for i in range(N):
                last_ci += copyList[i].count(1)
            break

    return answer, last_ci


def main():
    N, M = map(int, input().split())
    mapList = list()

    for _ in range(N):
        mapList.append(list(map(int, input().split())))

    answer = solution(N, M, mapList)
    print(answer[0])
    print(answer[1])


if __name__ == "__main__":
    main()

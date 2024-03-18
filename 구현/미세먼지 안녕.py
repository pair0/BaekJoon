import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    queue = deque()


# 공기청정기는 항상 1번 열 설치 (2개의 행을 차지)
# 미세먼지는 인접한 네 방향으로 확산
# 단, 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산 X
# 확산되는 양 : A(r,c) / 5 (소수점은 버림)
# (r,c)에 남은 미세먼지의 양은 A(r,c) - LA(R,C)/5x(확산된 방향의 개수)


# 공기청정기 작동 (반시계 방향으로 순환(위쪽), 시계방향 (아래쪽))
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 킨씩 이동
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람, 공기청정기로 들어간 미세먼지는 모두 정화
def solution(R, C, T, mapList):
    answer = 0

    # 상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    updx = [1, 0, -1, 0]
    updy = [0, -1, 0, 1]

    downdx = [1, 0, -1, 0]
    downdy = [0, 1, 0, -1]

    for i in range(1, R + 1):
        if mapList[i][0] == -1:
            airc = (i, 0)
            break

    for i in range(T):
        # 확산
        addmapList = [[0] * (C) for _ in range(R + 2)]
        for i in range(1, R + 1):
            for j in range(C):
                if mapList[i][j] >= 5:
                    total = 0
                    for k in range(4):
                        nx = j + dx[k]
                        ny = i + dy[k]

                        if 0 <= nx < C and 1 <= ny < R + 1 and mapList[ny][nx] != -1:
                            addmapList[ny][nx] += mapList[i][j] // 5
                            total += mapList[i][j] // 5
                    mapList[i][j] -= total
        for i in range(1, R + 1):
            for j in range(C):
                mapList[i][j] += addmapList[i][j]

        # 공기청정기 작동
        y, x = airc[0], airc[1] + 1
        y1, x1 = airc[0] + 1, airc[1] + 1
        burffer, burffer1 = deque([0]), deque([0])

        for a in range(4):
            while 1:
                nx = x + updx[a]
                ny = y + updy[a]
                if 0 <= nx < C and 1 <= ny < R + 1 and mapList[ny][nx] != -1:
                    burffer.append(mapList[y][x])
                    mapList[y][x] = burffer.popleft()
                    x, y = nx, ny

                else:
                    break

            while 1:
                nx1 = x1 + downdx[a]
                ny1 = y1 + downdy[a]

                if 0 <= nx1 < C and 1 <= ny1 < R + 1 and mapList[ny1][nx1] != -1:
                    burffer1.append(mapList[y1][x1])
                    mapList[y1][x1] = burffer1.popleft()
                    x1, y1 = nx1, ny1

                else:
                    break
        mapList[y][x] = burffer.popleft()
        mapList[y1][x1] = burffer1.popleft()

    for i in range(1, R + 1):
        for j in range(C):
            if mapList[i][j] > 0:
                answer += mapList[i][j]
    return answer


def main():
    R, C, T = map(int, input().split())
    mapList = list()
    mapList.append([0] * C)
    for _ in range(R):
        mapList.append(list(map(int, input().split())))
    mapList.append([0] * C)
    print(solution(R, C, T, mapList))


if __name__ == "__main__":
    main()

import sys
from collections import defaultdict, deque

input = sys.stdin.readline

parent = [0] * (1 + 1)


# # 유니온 파인드 알고리즘 사용
# def find_parent(x):
#     # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]


# def union(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b


def bfs(key, N, M, map, dx, dy, visited):
    queue = deque([key])
    visited[key[0]][key[1]] = True

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < M and 0 <= ny < N and not visited[ny][nx] and map[ny][nx] > 0:
                visited[ny][nx] = True
                queue.append((ny, nx))


# 0 : 바다, 0보다 큰 수 : 빙산의 높이
# 빙산의 높이는 일년마다 그 칸에 동서남북 네 방향으로 붙어있는 0이 저장된 칸의 개수만큼 줄어든다.
# 빙산이 두 덩어리 이상으로 분리되는 최초의 시간(년) 구하기
# 만약 전부 다 녹을 때까지 두 덩어리 이상으로 분리되지 않으면 0
def solution(mapList):
    answer = 0
    mapN = len(mapList)
    mapM = len(mapList[0])
    ice = defaultdict(int)

    for i in range(mapN):
        for j in range(mapM):
            if mapList[i][j] > 0:
                ice[(i, j)] = mapList[i][j]

    # 동서남북 정의
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0
    while len(ice) > 0:
        visited = [[False] * mapM for _ in range(mapN)]
        nodeCount = 0
        for key, value in ice.items():
            if not visited[key[0]][key[1]]:
                nodeCount += 1
                if nodeCount >= 2:
                    return count
                bfs(key, mapN, mapM, mapList, dx, dy, visited)
        count += 1
        popList = list()
        for key, value in ice.items():
            sea = 0
            for i in range(4):
                y = key[0] + dy[i]
                x = key[1] + dx[i]
                if 0 <= y < mapN and 0 <= x < mapM and mapList[y][x] == 0:
                    sea += 1

            if value - sea > 0:
                ice[key] = value - sea
            else:
                ice[key] = 0
                popList.append(key)

        for key, value in ice.items():
            mapList[key[0]][key[1]] = value

        for pop in popList:
            ice.pop(pop)

    return answer


def main():
    # 행의 개수, 열의 개수 (3<= N,M <= 300)
    N, M = map(int, input().split())
    mapList = list()
    for _ in range(N):
        mapList.append(list(map(int, input().split())))

    print(solution(mapList))


if __name__ == "__main__":
    main()

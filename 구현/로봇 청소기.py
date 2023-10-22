from collections import deque
import sys

input = sys.stdin.readline


def bfs(graph, r, c, d):
    global answer
    queue = deque([(r, c)])

    # 0 : 북, 1 : 동, 2 : 남, 3 : 서
    # 남서북동 정의
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    while queue:
        r, c = queue.popleft()
        if graph[r][c] == 0:
            graph[r][c] = 2
            answer += 1
        flag2 = 0
        flag3 = 0

        for i in range(4):
            nx = c + dx[i]
            ny = r + dy[i]

            # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우 탐색
            if ny < 0 or ny >= N or nx < 0 or nx >= M or graph[ny][nx] != 0:
                flag2 += 1
            # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우 탐색
            if 0 <= ny < N and 0 <= nx < M and graph[ny][nx] == 0:
                flag3 = 1
                break

        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 아에 없는 경우
        if flag2 == 4:
            if graph[r + dy[d]][c + dx[d]] != 1:  # 후진 가능하면 후진
                queue.append((r + dy[d], c + dx[d]))
            else:  # 불가능 하면 종료
                break
        # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우
        elif flag3 == 1:
            while True:
                # 90도 회전
                if d == 0:
                    d = 3
                else:
                    d -= 1
                # 90도 회전 후 앞칸이 청소되지 않은 빈칸이면 전진
                if graph[r + dy[d - 2]][c + dx[d - 2]] == 0:
                    queue.append((r + dy[d - 2], c + dx[d - 2]))
                    break


if __name__ == "__main__":
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    bfs(graph, r, c, d)
    print(answer)


from itertools import 
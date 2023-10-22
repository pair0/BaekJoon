import sys
from collections import deque
input = sys.stdin.readline

def change(d, c):
    # 상(0) 우(1) 하(2) 좌(3)
    # 동쪽 회전: 상(0) -> 우(1) -> 하(2) -> 좌(3) -> 상(0) : +1 방향
    # 왼쪽 회전: 상(0) -> 좌(3) -> 하(2) -> 우(1) -> 상(0) : -1 방향
    if c == "L":
        d = (d - 1) % 4
    else:
        d = (d + 1) % 4
    return d

# 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

def solution():
    answer = 1 #시간
    direction = 1 #초기 방향
    x, y = 0, 0 #초기 뱀 위치
    queue = deque([(x, y)])
    graph[y][x] = 2
    while(1):
        x, y = x + dx[direction], y + dy[direction]
        if 0 <= y < N and 0 <= x < N and graph[y][x] != 2:
            if not graph[y][x] == 1: # 사과가 없는 경우
                temp_x, temp_y = queue.popleft()
                graph[temp_y][temp_x] = 0 #꼬리 제거
            graph[y][x] = 2
            queue.append((x, y))
            if answer in times.keys():
                direction = change(direction, times[answer])
            answer += 1
        else:
            return answer


if __name__ == "__main__":
    N = int(input())
    K = int(input())
    graph = [[0]*N for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        graph[a-1][b-1] = 1
    L = int(input())
    times = {}
    for i in range(L):
        X, C = input().split()
        times[int(X)] = C
    print(solution())

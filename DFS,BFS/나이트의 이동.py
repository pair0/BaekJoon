import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, current, move):
    global answer
    queue = deque([current])
    graph[current[1]][current[0]] = 0
    
    ### 나이트 움직임 정의
    dx = [2, 1, 2, 1, -2, -1, -2, -1]
    dy = [-1, -2, 1, 2, 1, 2, -1, -2]

    while queue:
        x, y = queue.popleft()

        if (x, y) == move:
            answer.append(graph[y][x])

        for i in range(8):
            nx = x + dx[i] 
            ny = y + dy[i]

            if 0 <= nx < l and 0 <= ny < l and not graph[ny][nx] != -1:
                queue.append((nx, ny))
                graph[ny][nx] = graph[y][x] + 1

if __name__ == "__main__":
    T = int(input())
    for test_case in range(T):
        l = int(input())
        graph = [[-1] * l for _ in range(l)]
        current = tuple(map(int, input().split()))
        move = tuple(map(int, input().split()))
        answer = list()
        bfs(graph, current, move)
        print(min(answer))

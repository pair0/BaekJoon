import sys
input = sys.stdin.readline
from collections import deque

def bfs(start, end):
    queue = deque([start])
    visited[start] = True


    ### 수빈이의 이동 경우
    dx = [2, -1, 1]

    while queue:
        start = queue.popleft()

        if start == end:
            return graph[start]

        for i in range(3):
            if i > 0:
                nx = start + dx[i]
            else:
                nx = start * dx[i]
            
            if 0 <= nx <=100000 and not visited[nx]:
                queue.append(nx)
                visited[nx] = True
                if i > 0:
                    graph[nx] = graph[start] + 1
                else:
                    graph[nx] = graph[start]


if __name__ == "__main__":
    graph = [0] * 100001
    visited = [False] * 100001
    answer = list()
    N, K = map(int, input().split())

    print(bfs(N, K))
    

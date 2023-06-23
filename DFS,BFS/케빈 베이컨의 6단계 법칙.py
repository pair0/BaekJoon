import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, a, b):
    visited = [False] * (N+1)
    queue = deque([(a, 0)])
    visited[a] = True

    while queue:
        x, cnt = queue.popleft()

        if x == b:
            return cnt
        
        for i in graph[x]:
            if not visited[i]:
                queue.append((i, cnt+1))
                visited[i] = True


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    min_value = 98765432
    answer = 0

    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].append(B)
        graph[B].append(A)

    for i in range(1, N+1):
        temp = 0
        for j in range(1, N+1):
            if i == j:
                continue
            temp += bfs(graph, i, j)
        if min_value > temp:
            min_value = temp
            answer = i
    
    print(answer)


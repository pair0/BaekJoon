import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, visited):
    queue = deque([(start)])
    visited[start] = True

    while queue:
        start = queue.popleft()
        for i in graph[start]:
            if not visited[i]:
                answer[i] = start
                queue.append(i)
                visited[i] = True
        
def dfs(graph, v,visited):
    visited[v]=True
    for i in graph[v]:
        if not visited[i]:
            answer[i]=v
            dfs(graph, i, visited)

if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)
    answer = [0] * (N+1)
    for i in range(N-1):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    bfs(1, visited)
    # dfs(graph, 1, visited)

    for i in range(2, N+1):
        print(answer[i])
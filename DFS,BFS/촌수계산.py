import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end, graph):
    queue = deque([(start)])
    visited[start] = 0

    while queue:
        start = queue.popleft()

        if start == end:
            return 

        for i in graph[start]:
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[start] + 1


if __name__ == "__main__":
    n = int(input())
    p1, p2 = map(int, input().split())
    m = int(input())
    graph = [[] for _ in range(n+1)]
    visited = [-1 for _ in range(n+1)]

    for i in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    bfs(p1, p2, graph)
    print(visited[p2])
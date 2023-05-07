import sys
from collections import deque

Computer = int(sys.stdin.readline())
network = int(sys.stdin.readline())

graph = [[] for _ in range(Computer+1)]
visited = [0] * (Computer+1)

for i in range(network):
    N, M = map(int, sys.stdin.readline().split(" "))
    graph[N] += [M]
    graph[M] += [N]

def dfs(v):
    #방문한 한 노드
    visited[v] = 1

    #방문한 노드를 기반으로 탐색
    for node in graph[v]:
        if visited[node] == 0:
            dfs(node)

def bfs(v):
    queue = deque()
    #방문할 노드
    queue.append((v))
    visited[v] = 1

    while queue:
        #방문한 노드
        c = queue.popleft()

        #방문한 노드 기반으로 탐색
        for node in graph[c]:
            if visited[node] == 0:
                queue.append((node))
                visited[node] = 1


dfs(1)
print(sum(visited)-1)


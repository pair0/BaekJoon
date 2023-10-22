import sys

input = sys.stdin.readline

def dfs(idx, depth, visited):
    global answer
    visited[idx] = True

    if depth == 4:
        answer = True
        return 
    
    for i in graph[idx]:
        if not visited[i]:
            dfs(i, depth+1, visited)
            visited[i] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    parents = list(range(N))
    answer = False
    visited = [False] * N
    for i in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(N):
        dfs(i, 0, visited)
        visited[i] = False
        if answer:
            break

    if answer:
        print(1)
    else:
        print(0)


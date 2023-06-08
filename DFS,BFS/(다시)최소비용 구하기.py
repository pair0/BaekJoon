# ### 시간초과...
# import sys
# input = sys.stdin.readline

# def dfs(start, end, money, visited):
#     global answer
#     if start == end:
#         if answer == -1:
#             answer = money
#         elif answer > money:
#             answer = money 
#         return 

#     for i, j in graph[start]:
#         if not visited[i]:
#             visited[i] = True
#             dfs(i, end, money+j, visited)
#             visited[i] = False

# if __name__ == "__main__":
#     N = int(input())
#     M = int(input())
#     money = 0
#     answer = -1
#     graph = [[] for _ in range(N+1)]
#     visited = [False] * (N+1)
#     for i in range(M):
#         start, end, pay = map(int, input().split())
#         graph[start].append((end, pay))
#     S, E = map(int, input().split())
#     dfs(S, E, money, visited)
#     print(answer)

### 시간초과... bfs()
# import sys
# from collections import deque
# input = sys.stdin.readline

# def bfs(start):
#     queue = deque([start])

#     while queue:
#         start = queue.popleft()

#         for i, j in graph[start]:
#             min_pay = min(visited[start])
#             visited[i].append(j + min_pay)
#             queue.append(i)



# if __name__ == "__main__":
#     N = int(input())
#     M = int(input())
#     money = 0
#     answer = -1
#     graph = [[] for _ in range(N+1)]
#     visited = [[] for _ in range(N+1)]
#     visited[1].append(0)
#     for i in range(M):
#         start, end, pay = map(int, input().split())
#         graph[start].append((end, pay))
#     S, E = map(int, input().split())
#     bfs(S)
#     print(min(visited[E]))

### dijkstra
import heapq
from sys import maxsize
import sys

def dijkstra(x):
    pq = []
    heapq.heappush(pq, (0, x))
    visited[x] = 0

    while pq:
        d, x = heapq.heappop(pq)

        if visited[x] < d:
            continue

        for nw, nx in graph[x]:
            nd = d + nw

            if visited[nx] > nd:
                heapq.heappush(pq, (nd, nx))
                visited[nx] = nd

if __name__ == "__main__":
    input = sys.stdin.readline

    N = int(input())
    M = int(input())

    graph = [[] for _ in range(N + 1)]
    visited = [maxsize] * (N + 1)
    for i in range(M):
        start, end, pay = map(int, input().split())
        graph[start].append((pay, end))

    S, E = map(int, input().split())

    dijkstra(S)

    print(visited[E])
from collections import deque
import sys

# dfs


def dfs(graph, V, visited=deque()):
    visited.append(V)  # 방문 처리
    print(V, end=" ")

    for w in range(len(graph[V])):
        if graph[V][w] == 1 and w not in visited:
            dfs(graph, w)


# bfs
def bfs(graph, V, visited=deque()):
    # 리스트를 써서 pop(0)하게 되면 시간복잡도가 O(N)이다.
    # 그래서 시간복잡도가 O(1)인 deque를 사용한다.
    queue = deque()
    queue.append(V)

    while (queue):
        visit = queue.popleft()
        visited.append(visit)
        print(visit, end=" ")
        for w in range(len(graph[visit])):
            if graph[visit][w] == 1 and w not in visited and w not in queue:
                queue.append(w)


N, M, V = map(int, sys.stdin.readline().split())

graph = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    # 간선 입력 받기
    m1, m2 = map(int, sys.stdin.readline().split())
    # 간선이 양방향이기 때문에 아래와 같이 [m1][m2]와 [m2][m1] 모두 1로 셋팅
    graph[m1][m2] = graph[m2][m1] = 1

dfs(graph, V)
print()
bfs(graph, V)

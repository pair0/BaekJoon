import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
build_time = [0] * (N+1)
graph = [[] for _ in range(N+1)]
in_Degree = [0] * (N+1)

for i in range(1, N+1):
    test = list(map(int, input().split()))
    build_time[i] = test[0]
    in_Degree[i] = len(test) - 2
    for j in test[1:-1]:
        graph[j].append(i)


queue = deque()
time = [0] *(N+1)

for i in range(1, N+1):
    if in_Degree[i] == 0:
        queue.append(i)
        time[i] = build_time[i]

while queue:
    build = queue.popleft()

    for i in graph[build]:
        time[i] = max(time[i], time[build] + build_time[i])
        in_Degree[i] -= 1
        if in_Degree[i] == 0:
            queue.append(i)

for i in range(1, N+1):
    print(time[i])

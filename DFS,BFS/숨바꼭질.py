import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())
visit = [0 for i in range(100001)]
answer = 0
### 걷기 (x-1), (x+1) => 초당
### 순간이동 (2*x) => 초당
dx = [-1, 1, 2]

queue = deque([(0, N)])
visit[N] == 1

while queue:
    s, x = queue.popleft()

    if x == K:
        answer = s
        break

    for i in range(3):
        if i != 2:
            nx = x + dx[i]
        else:
            nx = x * dx[i]
        
        if 0 <= nx <= 100000 and not visit[nx]:
            queue.append((s+1, nx))
            visit[nx] = 1

print(answer)
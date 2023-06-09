# ### 순열 풀이
# import sys
# from itertools import permutations
# input = sys.stdin.readline

# N, M = map(int, input().split())
# N_list = [i for i in range(1, N+1)]

# for i in permutations(N_list, M):
#     print(*i)

### 백트래킹 이론으로 푼 풀이
def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n+1):
        if visited[i]:
            continue
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        print(s)
        print(visited)
        visited[i] = False
            

n, m = map(int, input().split())
s = []
visited = [False] * (n+1)

dfs()
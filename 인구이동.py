import sys
input = sys.stdin.readline
from collections import deque


def solution(graph, hashmap, hashmap2, N, L, R):
    answer = 0

    #상하좌우 정의
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while 1:
        count = 0
        sumcon = [[] for _ in range(N*N+1)] 

        # 연합 시키기
        for i in range(N):
            for j in range(N):
                for k in range(4): #인접 구하기
                    y, x = i+dy[k], j+dx[k]
                    if 0 <= x < N and 0 <= y < N:
                        if L <= abs(graph[i][j] - graph[y][x]) <= R:
                            sumcon[hashmap2[(i, j)]].append(hashmap2[(y, x)])
                            count += 1

        if count == 0:
            break
        # 연합의 수 세기
        visited = [0] * len(sumcon)

        def bfs(start):
            count_con = 1
            visit_list = list()
            y, x = hashmap[start]
            count_sum = graph[y][x]
            queue = deque([(start)])
            visit_list.append(start)
            visited[start] = 1

            while queue:
                index = queue.popleft()

                for i in sumcon[index]:
                    if visited[i] == 0:
                        queue.append(i)
                        visit_list.append(i)
                        visited[i] = 1
                        y, x = hashmap[i]
                        count_sum += graph[y][x]
                        count_con += 1
            
            now_peo = count_sum//count_con

            for i in visit_list:
                y, x = hashmap[i]
                graph[y][x] = now_peo

        for i in range(1, N*N+1):
            if len(sumcon[i]) != 0 and visited[i] == 0:
                bfs(i)

        answer += 1

    return answer


if __name__ == "__main__":
    N, L, R = map(int, input().split())
    graph = list()
    count_index = 1
    hashmap = dict()
    hashmap2 = dict()

    for i in range(N):
        graph.append(list(map(int, input().split())))
        for j in range(N):
            hashmap[count_index] = hashmap.get(count_index, (i, j))
            hashmap2[(i, j)] = hashmap.get((i, j), count_index)
            count_index += 1
    
    print(solution(graph, hashmap, hashmap2, N, L, R))
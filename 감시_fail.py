import sys
input = sys.stdin.readline
from collections import deque
import copy

def dfs(x, y, cctv, N, M):
    #queue = deque([(x, y)])
    global graph
    max_vlaue = -1
    count_cctv = 0

    #상우하좌 정의
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    if cctv in [1, 3, 4]:
        for i in range(4):
            graph_tmp = copy.deepcopy(graph)
            count_cctv = 0
            nx = x + dx[i]
            ny = y + dy[i]
            if cctv == 1:
                while 1:
                    if 0 <= nx < M and 0 <= ny < N and graph_tmp[ny][nx] != 6:
                        if graph_tmp[ny][nx] == 0:
                            graph_tmp[ny][nx] = -1 # '#'표시 대체
                            nx = nx + dx[i]
                            ny = ny + dy[i]
                            count_cctv += 1
                        else:
                            nx = nx + dx[i]
                            ny = ny + dy[i]
                    else:
                        break
            elif cctv == 3:
                tmp = 0
                while 1:
                    dist = (i+tmp) % 4
                    if 0 <= nx < M and 0 <= ny < N and graph_tmp[ny][nx] != 6:
                        if graph_tmp[ny][nx] == 0:
                            graph_tmp[ny][nx] = -1 # '#'표시 대체
                            nx = nx + dx[dist]
                            ny = ny + dy[dist]
                            count_cctv += 1
                        else:
                            nx = nx + dx[dist]
                            ny = ny + dy[dist]
                    else:
                        if tmp == 0:
                            tmp += 1
                            nx = x + dx[(i+tmp) % 4]
                            ny = y + dy[(i+tmp) % 4]
                        else:
                            break
            else:
                tmp = 0
                while 1:
                    dist = (i+tmp) % 4
                    if 0 <= nx < M and 0 <= ny < N and graph_tmp[ny][nx] != 6:
                        if graph_tmp[ny][nx] == 0:
                            graph_tmp[ny][nx] = -1 # '#'표시 대체
                            nx = nx + dx[dist]
                            ny = ny + dy[dist]
                            count_cctv += 1
                        else:
                            nx = nx + dx[dist]
                            ny = ny + dy[dist]
                    else:
                        if tmp < 2:
                            tmp += 1
                            nx = x + dx[(i+tmp) % 4]
                            ny = y + dy[(i+tmp) % 4]
                        else:
                            break
            if max_vlaue < count_cctv:
                max_vlaue = count_cctv
                graph_copy = copy.deepcopy(graph_tmp)
        graph = copy.deepcopy(graph_copy)
        return max_vlaue
    
    elif cctv == 2:
        for i in range(2):
            graph_tmp = copy.deepcopy(graph)
            count_cctv = 0
            nx = x + dx[i]
            ny = y + dy[i]
            tmp = 0
            while 1:
                dist = (i+tmp) % 4
                if 0 <= nx < M and 0 <= ny < N and graph_tmp[ny][nx] != 6:
                    if graph_tmp[ny][nx] == 0:
                        graph_tmp[ny][nx] = -1 # '#'표시 대체
                        nx = nx + dx[dist]
                        ny = ny + dy[dist]
                        count_cctv += 1
                    else:
                        nx = nx + dx[dist]
                        ny = ny + dy[dist]
                else:
                    if tmp < 2:
                        tmp += 2
                        nx = x + dx[(i+tmp) % 4]
                        ny = y + dy[(i+tmp) % 4]
                    else:
                        break
            if max_vlaue < count_cctv:
                    max_vlaue = count_cctv
                    graph_copy = copy.deepcopy(graph_tmp)
        graph = copy.deepcopy(graph_copy)
        return max_vlaue

    else:
        graph_tmp = copy.deepcopy(graph)
        count_cctv = 0
        nx = x + dx[0]
        ny = y + dy[0]
        tmp = 0
        while 1:
            dist = (0+tmp) % 4
            if 0 <= nx < M and 0 <= ny < N and graph_tmp[ny][nx] != 6:
                if graph_tmp[ny][nx] == 0:
                    graph_tmp[ny][nx] = -1 # '#'표시 대체
                    nx = nx + dx[dist]
                    ny = ny + dy[dist]
                    count_cctv += 1
                else:
                    nx = nx + dx[dist]
                    ny = ny + dy[dist]
            else:
                if tmp < 4:
                    tmp += 1
                    nx = x + dx[(0+tmp) % 4]
                    ny = y + dy[(0+tmp) % 4]
                else:
                    break
        graph = copy.deepcopy(graph_tmp)
        return count_cctv


def solution(N, M, count):
    answer = count
    answer2 = count
    global graph
    graph_copy2 = copy.deepcopy(graph)
    cctv_list = {1:1, 2:2, 3:3, 4:4, 5:5}

    for i in range(N):
        for j in range(M):
            if graph[i][j] in cctv_list.keys():
                answer = answer - dfs(j, i, cctv_list[graph[i][j]], N, M)
    
    graph = copy.deepcopy(graph_copy2)
    for i in range(N-1, -1, -1):
        for j in range(M-1, -1, -1):
            if graph[i][j] in cctv_list.keys():
                answer2 = answer2 - dfs(j, i, cctv_list[graph[i][j]], N, M)
    
    return min(answer, answer2)

if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = list()
    count = 0
    for i in range(N):
        graph.append(list(map(int, input().split())))
        count += graph[i].count(0)
    
    print(solution(N, M, count))
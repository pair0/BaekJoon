import sys
input = sys.stdin.readline

def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a > b:
        parents[a] = b
    else:
        parents[b] = a

if __name__ == "__main__":
    N = int(input()) ### 200 이하 (도시)
    M = int(input()) ### 1000 이하
    graph = []
    parents = list(range(N))

    for _ in range(N):
        graph.append(list(map(int, input().split())))

    plan = list(map(int, input().split()))    
    print(graph)
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 1:
                union(i,j)
        print(parents)

    answer = "YES"
    for i in range(1, M):
        if parents[plan[i] - 1] != parents[plan[0] - 1]:
            answer = "NO"
            break
    
    print(answer)

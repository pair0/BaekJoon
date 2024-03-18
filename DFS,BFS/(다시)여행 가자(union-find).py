import sys

input = sys.stdin.readline

from collections import defaultdict


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
    edges = [
        [4, 11],
        [1, 12],
        [8, 3],
        [12, 7],
        [4, 2],
        [7, 11],
        [4, 8],
        [9, 6],
        [10, 11],
        [6, 10],
        [3, 5],
        [11, 1],
        [5, 3],
        [11, 9],
        [3, 8],
    ]

    answer = []
    N = max(sum(edges, []))
    graph = defaultdict(list)
    parents = list(range(N + 1))

    for edge in edges:
        graph[edge[0]].append(edge[1])

    print(graph)
    for i in range(1, N + 1):
        for j in range(len(graph[i])):
            union(i, j)
        print(parents)

    answer = "YES"
    # for i in range(1, M):
    #     if parents[plan[i] - 1] != parents[plan[0] - 1]:
    #         answer = "NO"
    #         break

    print(answer)

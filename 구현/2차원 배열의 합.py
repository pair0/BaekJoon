import sys
input = sys.stdin.readline

N, M = map(int, input().split())
list_int = [list(map(int, input().split())) for _ in range(N)]
K = int(input())

for _ in range(K):
    answer = 0
    i, j, x, y = map(int, input().split())

    for index in range(i, x+1):
        answer += sum(list_int[index-1][j-1:y])

    print(answer)

import sys
input = sys.stdin.readline

N = int(input())
answer = list()

peo = [list(map(int, input().split())) for _ in range(N)]

for i in peo:
    rank = 1
    for j in peo:
        if i[0] < j[0] and i[1] < j[1]:  # 키와 몸무게가 모두 커야 랭크 업
            rank += 1
    print(rank, end=" ")

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_map = list()

for _ in range(N):
    N_map.append(list(map(int, input().split())))

print(N_map)
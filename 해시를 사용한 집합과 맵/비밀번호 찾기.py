import sys

N, M = map(int, sys.stdin.readline().split(" "))
pass_map = {}

for i in range(N):
    key, value = sys.stdin.readline().strip().split(" ")
    pass_map[key] = value

for i in range(M):
    print(pass_map[sys.stdin.readline().strip()])

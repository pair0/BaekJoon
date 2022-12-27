import sys

num_hash = dict()

T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split(" "))
    num = list(map(int, sys.stdin.readline().split(" ")))
    for j in range(len(num)):
        num_hash[j] = num[j]

import sys

N = int(sys.stdin.readline())
number = list()

for _ in range(N):
    number.append(int(sys.stdin.readline()))

for i in range(N):
    for j in range(N-i-1, -1, -1):
        
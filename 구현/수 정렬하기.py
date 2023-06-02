import sys
input = sys.stdin.readline

N = int(input())
N_list = [0] * N

for i in range(N):
    N_list[i] = int(input())

for i in sorted(N_list):
    print(i)
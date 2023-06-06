import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
for i in range(E):
    u, v, w = map(int, input().split())

    
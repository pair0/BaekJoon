import sys
from collections import deque
input = sys.stdin.readline


K = int(input())
queue = deque()

for i in range(K):
    money = int(input())

    if money == 0:
        queue.pop()
    else:
        queue.append(money)

print(sum(queue))

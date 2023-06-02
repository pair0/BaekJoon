import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = [list(map(int, input().split())) for _ in range(N)]

queue.sort()
room = list()

heapq.heappush(room, queue[0][1])

for i in range(1, N):
    if room[0] > queue[i][0]:
        heapq.heappush(room, queue[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, queue[i][1])

print(len(room))
import sys
from collections import deque

T = int(sys.stdin.readline())

for test_case in range(T):
    N, M = map(int, sys.stdin.readline().split(" "))
    queue = deque(list(map(int, sys.stdin.readline().split(" "))))
    answer = 0

    while queue:
        first = max(queue)
        front = queue.popleft()
        M -= 1

        if first == front:
            answer += 1
            if M < 0:
                print(answer)
                break
        else:
            queue.append(front)
            if M < 0:  # 제일 앞에서 뽑히면 제일 뒤로 이동동
                M = len(queue) - 1

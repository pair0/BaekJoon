import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = deque()

for _ in range(N):
    S = input().strip()

    if "push_front" in S:
        x = S.split(" ")[1]
        stack.appendleft(x)
    elif "push_back" in S:
        x = S.split(" ")[1]
        stack.append(x)
    else:
        if "pop_front" == S:
            if len(stack) != 0:
                print(stack.popleft())
            else:
                print("-1")
        elif "pop_back" == S:
            if len(stack) != 0:
                print(stack.pop())
            else:
                print("-1")
        elif "size" == S:
            print(len(stack))
        elif "empty" == S:
            if len(stack) != 0:
                print("0")
            else:
                print("1")
        elif "front" == S:
            if len(stack) != 0:
                print(stack[0])
            else:
                print("-1")
        else:
            if len(stack) != 0:
                print(stack[-1])
            else:
                print("-1")

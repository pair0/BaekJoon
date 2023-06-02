import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
stack = deque()

for i in range(N):
    command = input().strip()
    
    if "push" in command:
        stack.append(command.split()[1])
    elif "pop" == command:
        if len(stack) == 0:
            print('-1')
        else:
            print(stack.pop())
    elif "size" == command:
        print(len(stack))
    elif "empty" == command:
        if len(stack) == 0:
            print('1')
        else:
            print('0')
    else:
        if len(stack) == 0:
            print('-1')
        else:
            print(stack[len(stack)-1])
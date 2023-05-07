import sys

N = int(sys.stdin.readline())
result = 0

A = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))
B = sorted(list(map(int, sys.stdin.readline().strip().split(" "))), reverse=True)

for i in range(len(A)):
    result += A[i] * B[i]

print(result)
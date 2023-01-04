import sys

zero = [1, 0, 1]
one = [0, 1, 1]

def fibonacci(n):
    if n <= 2:
        print(f"{zero[n]} {one[n]}")
    elif n > 2:
        while len(zero)-1 < n:
            zero.append(zero[len(zero)-1]+zero[len(zero)-2])
            one.append(one[len(one)-1]+one[len(one)-2])
        print(f"{zero[n]} {one[n]}")

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    fibonacci(N)

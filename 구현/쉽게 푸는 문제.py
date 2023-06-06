import sys
input = sys.stdin.readline


### 1 ~ 1000
arr = [0] * 1050
count = 1
index = 0

while index < 1000:
    for _ in range(count):
        arr[index] = count
        index += 1
    count += 1

A, B = map(int, input().split())

print(sum(arr[A-1:B]))
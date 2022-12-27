import sys

first = int(sys.stdin.readline())
second = sys.stdin.readline().strip()
result = 0

for i in range(len(second)):
    print(first*int(second[len(second)-i-1]))
    result += first*int(second[len(second)-i-1])*(10**i)

print(result)


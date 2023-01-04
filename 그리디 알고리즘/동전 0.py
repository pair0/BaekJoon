import sys

N, K = map(int, sys.stdin.readline().split(" "))
list_m = list()
count = 0

for i in range(N):
    list_m.append(int(sys.stdin.readline()))

list_m.sort(reverse=True)

for m in list_m:
    if m > K:
        continue
    elif m == K:
        count += 1
        break
    else:
        count += (K // m)
        K -= ((K // m) * m)

print(count)
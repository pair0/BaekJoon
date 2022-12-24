import sys

N, M = map(int, sys.stdin.readline().split(" "))
A = list(map(int, sys.stdin.readline().split(" ")))
B = list(map(int, sys.stdin.readline().split(" ")))
hash_map = {}
answer = 0

## dict 버전 : 284ms
for type in A+B:
    hash_map[type] = hash_map.get(type, -1) + 1

for key, value in hash_map.items():
    if value == 0:
        answer += 1

print(answer)


## list 버전 : 시간초과
# for i in range(N):
#     if A[i] in B:
#         answer += 1
# for i in range(M):
#     if B[i] in A:
#         answer += 1
# print(answer)

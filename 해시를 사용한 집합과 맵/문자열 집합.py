import sys

N, M = map(int, sys.stdin.readline().split(" "))

## dict 버전 : 112ms
list_hash = {}
answer = 0

for i in range(N):
    list_hash[sys.stdin.readline()] = 1

for i in range(M):
    if list_hash.get(sys.stdin.readline()):
        answer += 1
print(answer)

# ## list 버전 : 3712
# list = []
# answer = 0
#
# for i in range(N):
#     list.append(sys.stdin.readline())
#
# for i in range(M):
#     if sys.stdin.readline() in list:
#         answer += 1
#
# print(answer)

import sys

N, M = map(int, sys.stdin.readline().split())
list_hash = {}

for i in range(1, N+1):
    list_hash[i] = sys.stdin.readline().strip() ##strip: 줄바꿈 문자 제거

list_hash_rever = {v:k for k,v in list_hash.items()}

for i in range(M):
    answer = sys.stdin.readline().strip()
    if answer.isdigit(): ## isdigit() : 해당 문자열이 숫자로만 이루어졌는지 판별 => 문자열에 개행문자가 포함되어 있으면 숫자로만 이루어 져있어도 문자열로 판별
        print(list_hash.get(int(answer)))
    else:
        print(list_hash_rever.get(answer))

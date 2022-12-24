import sys

N, M = map(int, sys.stdin.readline().split())
list = []

for i in range(N):
    list.append(sys.stdin.readline().strip()) ##strip: 줄바꿈 문자 제거

for i in range(M):
    answer = sys.stdin.readline().strip()
    if answer.isdigit(): ## isdigit() : 해당 문자열이 숫자로만 이루어졌는지 판별 => 문자열에 개행문자가 포함되어 있으면 숫자로만 이루어 져있어도 문자열로 판별
        print(list[int(answer)-1])
    else:
        print(int(list.index(answer)) + 1)


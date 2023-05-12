import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())

for test_case in range(T):
    N = int(input())
    answer = 1
    grade = sorted([list(map(int, input().split()))
                   for _ in range(N)])
    man = grade[0][1]
    for i in range(1, N):
        if grade[i][1] < man:
            man = grade[i][1]
            answer += 1

    print(answer)

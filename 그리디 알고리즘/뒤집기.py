import sys
input = sys.stdin.readline

S = input().strip()
answer = 0

for i in range(len(S) - 1):
    if S[i] != S[i+1]:
        answer += 1

print((answer + 1)//2)

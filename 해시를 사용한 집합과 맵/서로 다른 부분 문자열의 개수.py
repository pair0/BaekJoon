import sys

S = sys.stdin.readline().strip()
answer = set()

for i in range(len(S)):
    for j in range(i, len(S)):
        answer.add(S[i:j+1])

print(len(answer))
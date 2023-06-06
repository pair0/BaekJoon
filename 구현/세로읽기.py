import sys
input = sys.stdin.readline

S = [[-1] * 15 for _ in range(5)]
max_len = 0

for i in range(5):
    s1 = input().strip()
    s_len = len(s1)
    if max_len < s_len:
        max_len = s_len
    S[i][:s_len] = s1

for i in range(max_len):
    for j in range(5):
        if S[j][i] == -1:
            continue
        print(S[j][i], end="")
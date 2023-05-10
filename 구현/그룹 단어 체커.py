import sys
input = sys.stdin.readline

N = int(input())
answer = 0

for _ in range(N):
    s = input()
    test = list()
    test.append(s[0])
    flag = 0

    for i in range(1, len(s)):
        if s[i] in test:
            if s[i] != test[-1]:
                flag = 1
                break
        else:
            test.append(s[i])

    if flag == 0:
        answer += 1

print(answer)

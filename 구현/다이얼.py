import sys
input = sys.stdin.readline
A_Z = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number_dict = dict()
count = 3
answer = 0

for i in A_Z:
    number_dict[i] = count
    if i in "CFILOSVZ":
        count += 1

S = input().strip()

for i in S:
    answer += number_dict[i]

print(answer)
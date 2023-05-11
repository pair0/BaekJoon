# import sys

# croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
# s = sys.stdin.readline()
# answer = 0
# i = 0

# while i != len(s) - 1:
#     if s[i:i+3] in croa:
#         i += 3
#     elif s[i:i+2] in croa:
#         i += 2
#     else:
#         i += 1
#     answer += 1

# print(answer)

import sys

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = sys.stdin.readline().strip()

for i in croatia:
    word = word.replace(i, '*')  # input 변수와 동일한 이름의 변수

print(len(word))

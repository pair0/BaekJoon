# import sys

# X = int(sys.stdin.readline())

# line = 1

# while X > line:  # 등차수열의 라인 수 구하기
#     X -= line
#     line += 1

# if line % 2 == 0:
#     a = X
#     b = line-X+1
# else:
#     a = line-X+1
#     b = X

# print(a, '/', b, sep='')


import sys
iniput = sys.stdin.readline

X = int(input())

line = 1

while X > line:
    X -= line
    line += 1

if line % 2 == 0:  # 짝수 라인인지 홀 수 라인인지 판별
    a = X  # 분자
    b = line - X + 1  # 분모
else:
    b = X
    a = line - X + 1

print(a, '/', b,  sep="")

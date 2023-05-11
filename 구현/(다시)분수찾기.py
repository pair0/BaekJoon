import sys


X = int(sys.stdin.readline())

line = 1

while X > line:  # 등차수열의 라인 수 구하기
    X -= line
    line += 1

if line % 2 == 0:
    a = X
    b = line-X+1
else:
    a = line-X+1
    b = X

print(a, '/', b, sep='')

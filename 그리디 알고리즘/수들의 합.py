import sys
input = sys.stdin.readline

S = int(input())
N = 1
sum_value = 1

while sum_value <= S:  # 1~N까지의 합이 S를 넘어가기 직전에 값이 최대값
    N += 1
    sum_value += N

print(N-1)

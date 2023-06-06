import sys
input = sys.stdin.readline

MAX = 1000000

dp = [0] * (MAX + 1) # 각 인덱스마다 약수의 합을 담아 높읗 배열
s = [0] * (MAX + 1) # 각 인덱스까지 누적합을 담을 배열

for i in range(1, MAX+1): # 1부터 최대값까지 구하기
    j = 1 # i에 곱할 j를 선언
    while i * j <= MAX:
        dp[i*j] += i
        j += 1 #j값 증가
    s[i] = s[i - 1] + dp[i] #해당 dp[i]의 값까지 더한 누적합을 s배열에

T = int(input())
for test_case in range(T):
    N = int(input())
    print(s[N])
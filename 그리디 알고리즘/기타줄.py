import sys
input = sys.stdin.readline

N, M = map(int, input().split())
price = [list(map(int, input().split())) for _ in range(M)]
price_package = sorted(price)[0][0]
price_single = sorted(price, key=lambda x: x[1])[0][1]
answer = 0

while N > 0:
    if N >= 6:
        if (N//6) * price_package <= (N//6) * (price_single * 6):
            answer += ((N//6) * price_package)
        else:
            answer += (N//6) * (price_single * 6)
        N %= 6
    else:
        if price_package <= price_single * N:
            answer += price_package
        else:
            answer += price_single * N
        N = 0

print(answer)

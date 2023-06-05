import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

T = int(input())
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
Nsum = list()
Msum = list()

for i in range(n): ### N_list의 구간 합 모두 구하기
    s = n_list[i]
    Nsum.append(s)
    for j in range(i+1, n):
        s+=n_list[j]
        Nsum.append(s)
for i in range(m): ### m_list의 구간 합 모두 구하기
    s = m_list[i]
    Msum.append(s)
    for j in range(i+1, m):
        s+=m_list[j]
        Msum.append(s)

Nsum.sort()
Msum.sort()
answer = 0

for i in range(len(Nsum)):
    l = bisect_left(Msum, T-Nsum[i])
    r = bisect_right(Msum, T-Nsum[i])
    answer+=r-l

print(answer)

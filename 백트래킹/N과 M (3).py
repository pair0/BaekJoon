### 중복 순열 풀이
import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]

for i in product(N_list, repeat = M):
    print(*i)

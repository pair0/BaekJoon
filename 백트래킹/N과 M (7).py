### 중복 순열 풀이
import sys
from itertools import product
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

for i in product(N_list, repeat = M):
    print(*i)

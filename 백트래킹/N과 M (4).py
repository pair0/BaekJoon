### 중복 조합 풀이
import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = [i for i in range(1, N+1)]

for i in combinations_with_replacement(N_list, M):
    print(*i)

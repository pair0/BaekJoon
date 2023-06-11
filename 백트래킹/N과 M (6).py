### 조합 풀이
import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

for i in combinations(N_list, M):
    print(*i)

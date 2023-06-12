# ### 순열 풀이
import sys
from itertools import permutations
input = sys.stdin.readline

N, M = map(int, input().split())
N_list = sorted(list(map(int, input().split())))

for i in permutations(N_list, M):
    print(*i)

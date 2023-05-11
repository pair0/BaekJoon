import sys
# from statistics import *
# from collections import Counter
input = sys.stdin.readline

N = int(input())
number = [int(input()) for _ in range(N)]

# 산술평균
print(round(sum(number)/N))
# print(round(mean(number)))

# 중앙값
print(sorted(number)[len(number)//2])
# print(median(number))

# 최빈값
hash_count = dict()
for i in number:
    hash_count.setdefault(i, 0)
    hash_count[i] += 1

hash_count = dict(sorted(hash_count.items()))
hash_count = dict(sorted(hash_count.items(), key=lambda x: x[1], reverse=True))
if len(hash_count) > 1 and list(hash_count.values())[0] == list(hash_count.values())[1]:
    print(list(hash_count.keys())[1])
else:
    print(list(hash_count.keys())[0])
# if len(Counter(sorted(number)).most_common(2)) > 1 and Counter(sorted(number)).most_common(2)[0][1] == Counter(sorted(number)).most_common(2)[1][1]:
#     print(Counter(sorted(number)).most_common(2)[1][0])
# else:
#     print(Counter(sorted(number)).most_common(2)[0][0])

# 범위
print(max(number) - min(number))

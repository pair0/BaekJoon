import sys

N = int(sys.stdin.readline())
num_hash = {}

for i in range(N):
    number = int(sys.stdin.readline().strip())
    num_hash[number] = num_hash.get(number, 0) + 1

num_hash = dict(sorted(num_hash.items())) ## 딕셔너리 sorted
print(max(num_hash, key=num_hash.get)) ## 딕셔너리 max 추출

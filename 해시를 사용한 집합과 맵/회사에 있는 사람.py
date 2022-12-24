import sys

n = int(sys.stdin.readline())
people_hash = dict()

for i in range(n):
    key, value = sys.stdin.readline().strip().split(" ")
    people_hash[key] = value

people_hash = dict(sorted(people_hash.items(), reverse=True))
for k, v in people_hash.items():
    if v == "enter":
        print(k)

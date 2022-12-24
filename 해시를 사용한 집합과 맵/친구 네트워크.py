import sys
---

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    F = int(sys.stdin.readline())
    network_hash = dict()

    for _ in range(F):
        key, value = sys.stdin.readline().strip().split(" ")
        network_hash[key] = value
        network_hash[value] = key


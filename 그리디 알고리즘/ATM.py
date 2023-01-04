import sys

N = int(sys.stdin.readline())
P_list = sorted(list(map(int, sys.stdin.readline().strip().split(" "))))

for i in range(len(P_list)):
    if i == 0:
        continue
    else:
        P_list[i] = P_list[i] + P_list[i-1]

print(sum(P_list))
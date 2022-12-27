import sys

T = int(sys.stdin.readline())

for i in range(T):
    N = int(sys.stdin.readline())
    N_list = list(map(int, sys.stdin.readline().split(" ")))
    M = int(sys.stdin.readline())
    M_list = list(map(int, sys.stdin.readline().split(" ")))
    N_list = dict.fromkeys(N_list, 1) ##list를 dict로 변환
    for j in range(M):
        if N_list.get(M_list[j]):
            print("1")
        else:
            print("0")
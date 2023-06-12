import sys
input = sys.stdin.readline

def binary(i, N, start, end):
    if start > end:
        return 0
    m = (start+end)//2
    if i == N[m]:
        return 1
    elif i < N[m]:
        return binary(i, N, start, m-1)
    else:
        return binary(i, N, m+1, end)

if __name__ == "__main__":
    N = int(input())
    N_list = sorted(list(map(int, input().split())))
    M = int(input())
    M_list = list(map(int, input().split()))

    for i in M_list:
        start = 0
        end = N - 1
        print(binary(i, N_list, start, end))

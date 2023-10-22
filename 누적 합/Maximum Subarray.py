import sys

input = sys.stdin.readline

def solution(N, X):
    max_v = -99999
    sum_v = 0
    sum_list = [0]

    for i in range(N):
        sum_v += X[i]
        sum_list.append(sum_v)
        
    for i in range(N, 0, -1):
        for j in range(i-1, -1, -1):
            if max_v < sum_list[i] - sum_list[j]:
                max_v = sum_list[i] - sum_list[j]

    return max_v

if __name__ == "__main__":
    T = int(input())
    for test_case in range(T):
        N = int(input())
        X = list(map(int, input().split()))
        print(solution(N, X))
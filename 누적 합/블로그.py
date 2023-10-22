import sys

sys = sys.stdin.readline

def solution(N, X, N_list):
    answer = 0
    sum_list = [0]
    sum_v = 0
    count = 1

    for i in range(N):
        sum_v += N_list[i]
        sum_list.append(sum_v)

    if sum_list[-1] == 0:
        return ["SAD", -1]
    
    for i in range(N, X-1, -1):
        if answer < sum_list[i] - sum_list[i-X]:
            count = 1
            answer = sum_list[i] - sum_list[i-X]
        elif answer == sum_list[i] - sum_list[i-X]:
            count += 1

    return [answer, count]

if __name__ == "__main__":
    N, X = map(int, input().split())
    N_list = list(map(int, input().split()))

    result = solution(N, X, N_list)
    if result[1] == -1:
        print(result[0])
    else:
        print(result[0])
        print(result[1])
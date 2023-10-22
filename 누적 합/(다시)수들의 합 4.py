import sys

input = sys.stdin.readline

def solution(N, K, A):
    answer = 0
    sum_dic = {0: 1}
    sum_v = 0

    for i in A:
        sum_v += i

        if sum_v-K in sum_dic.keys():
            answer += sum_dic[sum_v-K]
        
        sum_dic[sum_v] = sum_dic.get(sum_v, 0) + 1
    return answer

if __name__ == "__main__":
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    print(solution(N, K, A))
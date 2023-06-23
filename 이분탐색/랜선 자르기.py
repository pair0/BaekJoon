import sys
input = sys.stdin.readline

def binary(len_length, N):
    start = 1
    end = max(len_length)
    answer = 0

    while start <= end:
        total = 0
        mid = (start + end) // 2

        for i in len_length:
            total += i // mid
        
        if total >= N:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return answer

if __name__ == "__main__":
    K, N = map(int, input().split())
    len_length = list()
    for i in range(K):
        len_length.append(int(input()))
    print(binary(len_length, N))

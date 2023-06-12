import sys
input = sys.stdin.readline

def binary(tree_hei, M):
    start = 0
    end = max(tree_hei)
    answer = 0

    while start <= end:
        total = 0
        mid = (start + end) // 2
        
        for height in tree_hei:
            if height > mid:
                total += height - mid
        
        if total >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    
    return answer

if __name__ == "__main__":
    N, M = map(int, input().split())
    tree_hei = sorted(list(map(int, input().split())))
    print(binary(tree_hei, M))



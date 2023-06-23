import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N, M, B = map(int, input().split())
    answer_time = (255 *2) * (500*500) 
    answer_h = 0 
    ground = list()
    for _ in range(N):
        ground.append(list(map(int, input().split())))
    
    for h in range(256+1):
        remove = 0
        append = 0
        for i in ground:
            for j in i:
                height = j - h
                if height < 0:
                    append -= height
                else:
                    remove += height
        if remove + B >= append:
            times = remove*2 + append
            if answer_time >= times:
                answer_time = times
                answer_h = h
    
    print(answer_time, answer_h)
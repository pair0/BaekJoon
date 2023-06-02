import sys
input = sys.stdin.readline
total = 0
sum_list = [0]

for _ in range(10):
    score = int(input())
    total += score
    sum_list.append(total)

if sum_list[10] < 100: ### 총 합이 100이 안넘으면 총 합을 출력
    print(sum_list[10])
    exit()

for i in range(1, 10+1):
    if sum_list[i] == 100:
        print(sum_list[i])
        exit()
    elif sum_list[i] > 100:
        if sum_list[i] - 100 <= 100 - sum_list[i-1]:
            print(sum_list[i])
            exit()
        else:
            print(sum_list[i-1])
            exit()
    
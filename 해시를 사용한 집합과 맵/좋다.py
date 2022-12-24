import sys

N = int(sys.stdin.readline())
number_list = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0

for i in range(N):
    tmp = number_list[:i] + number_list[i+1:]
    left, right = 0, len(tmp) - 1
    while left < right:
        sum = tmp[left] + tmp[right]
        if sum == number_list[i]:
            answer += 1
            break
        if sum < number_list[i]:
            left += 1
        else:
            right -= 1

print(answer)
import sys
input = sys.stdin.readline

x_list = list()
for _ in range(4):
    x_list.append(list(map(int, list(input().strip()))))

K = int(input())
for i in range(K):
    number, direction = map(int, input().split())
    flag = [False, x_list[0][2] != x_list[1][6], x_list[1][2] != x_list[2][6], x_list[2][2] != x_list[3][6], False]
    flag2 = 0
    flag3 = 0

    if direction > 0:  # 시계방향
        x_list[number-1] = [x_list[number-1][7]] + x_list[number-1][:7]
        for j in range(number - 1, 0, -1):
            if not flag[j]:
                break
            if flag2 % 2 == 0:
                x_list[j-1] = x_list[j-1][1:] + [x_list[j-1][0]]
            else:
                x_list[j-1] = [x_list[j-1][7]] + x_list[j-1][:7]
            flag2 += 1
        for j in range(number, 4):
            if not flag[j]:
                break
            if flag3 % 2 == 0:
                x_list[j] = x_list[j][1:] + [x_list[j][0]]
            else:
                x_list[j] = [x_list[j][7]] + x_list[j][:7]
            flag3 += 1

    else: # 역시계 방향
        x_list[number-1] = x_list[number-1][1:] + [x_list[number-1][0]]    
        for j in range(number - 1, 0, -1):
            if not flag[j]:
                break
            if flag2 % 2 == 0:
                x_list[j-1] = [x_list[j-1][7]] + x_list[j-1][:7]
            else:
                x_list[j-1] = x_list[j-1][1:] + [x_list[j-1][0]]
            flag2 += 1
        for j in range(number, 4):
            if not flag[j]:
                break
            if flag3 % 2 == 0:
                x_list[j] = [x_list[j][7]] + x_list[j][:7]
            else:
                x_list[j] = x_list[j][1:] + [x_list[j][0]]
            flag3 += 1

print(x_list[0][0] + x_list[1][0] * 2 + x_list[2][0] * 4 + x_list[3][0] * 8)
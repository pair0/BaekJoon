import sys

N = int(sys.stdin.readline())
number_list = sorted(list(map(int, sys.stdin.readline().split())))

hash_map_e = {} #list 중 짝수 저장
hash_map_o = {} #list 중 홀수 저장
count = 0

for key in number_list:
    if key % 2 == 0:
        hash_map_e[key] = hash_map_e.get(key, 0) + 1
    elif key % 2 != 0:
        hash_map_o[key] = hash_map_o.get(key, 0) + 1

for i in range(N-1, 0, -1):
    flag = 0
    if number_list[i] % 2 == 0: #짝수 일 때wjd
        if number_list[i]/2 in hash_map_e and hash_map_e[number_list[i]/2] >= 2:
            count += 1
            continue
        else:
            for e in reversed(hash_map_e): #짝수 + 짝수
                if e <= number_list[i]:
                    for e_1 in hash_map_e:
                        if e_1 == e:
                            break
                        elif e + e_1 == number_list[i]:
                            count += 1
                            flag = 1
                            break
                if flag == 1:
                    break

            if flag == 0:
                for e in reversed(hash_map_o):  # 홀수 + 홀수
                    if e <= number_list[i]:
                        for e_1 in hash_map_o:
                            if e_1 == e:
                                break
                            elif e + e_1 == number_list[i]:
                                count += 1
                                flag = 1
                                break
                    if flag == 1:
                        break

    else: #홀수 일 때
        for o in hash_map_e:
            if o <= number_list[i]:
                for o_1 in hash_map_o:
                    if o + o_1 == number_list[i]:
                        count += 1
                        flag = 1
                        break
            if flag == 1:
                break

print(count)




make_list = list()

for i in range(1, 10001):
    make_number = i
    if i < 10:
        i_list = list(map(int, str(i)))
        i_list.insert(0, 0)
    else:
        i_list = list(map(int, str(i)))

    for j in i_list:
        make_number += j
    make_list.append(make_number)


for i in range(1, 10001):
    if i not in sorted(make_list):
        print(i)

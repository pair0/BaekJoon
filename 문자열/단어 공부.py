# import sys
## dict 방식 (메모리 : 32432, 시간 : 200)
# String = sys.stdin.readline().strip().upper()
# string_dic = dict()
#
# for i in String:
#     string_dic[i] = string_dic.get(i, 0) + 1
#
# list_dict = sorted(list(string_dic.values()), reverse=True)
# if len(string_dic) == 1:
#     print(list(string_dic.keys())[0])
# elif list_dict[0] == list_dict[1]:
#     print("?")
# else:
#     print(max(string_dic, key=string_dic.get)) ## 최대 value에 대한 key 찾기

## list 방식 (메모리 : 32424, 시간 : 76)
import sys
string = sys.stdin.readline().strip().upper()
string_list = list(set(string))
cnt = []

for i in string_list:
    cnt.append(string.count(i))

if cnt.count(max(cnt)) >= 2:
    print("?")
else:
    print(string_list[cnt.index(max(cnt))])
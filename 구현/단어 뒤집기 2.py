# import sys
# input = sys.stdin.readline

# S = input().strip()
# flag = 0
# tag = ''
# str1 = ''

# for i in S:
#     if i == '<' or flag == 1:
#         if str1 != '':
#             print(''.join(str1[::-1]), end="")
#             str1 = ''
#         flag = 1
#         tag += i
#         if i == '>':
#             flag = 0
#             print(tag, end="")
#             tag = ''
#     else:
#         if i == ' ':
#             print(''.join(str1[::-1]), end=" ")
#             str1 = ''
#             continue
#         str1 += i

# if str1 != '':
#     print(''.join(str1[::-1]), end="")
#     str1 = ''


# 다른 풀이
import sys
word = list(sys.stdin.readline().rstrip())

i = 0
start = 0

while i < len(word):
    if word[i] == "<":       # 열린 괄호를 만나면
        i += 1
        while word[i] != ">":      # 닫힌 괄호를 만날 때 까지
            i += 1
        i += 1               # 닫힌 괄호를 만난 후 인덱스를 하나 증가시킨다
    elif word[i].isalnum():  # 숫자나 알파벳을 만나면
        start = i
        while i < len(word) and word[i].isalnum():
            i += 1
        tmp = word[start:i]  # 숫자,알파벳 범위에 있는 것들을
        tmp.reverse()       # 뒤집는다
        word[start:i] = tmp
    else:                   # 괄호도 아니고 알파,숫자도 아닌것 = 공백
        i += 1                # 그냥 증가시킨다

print("".join(word))

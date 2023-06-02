import sys
input = sys.stdin.readline

alpa = 'abcdefghijklmnopqrstuvwxyz'
S = input().strip()
dict_S = dict()

for index, value in enumerate(S):
    if dict_S.get(value) != None:
        continue
    dict_S[value] = index

for i in alpa:
    if i in S:
        print(dict_S[i], end=" ")
    else:
        print('-1', end=" ")
    

import sys
input = sys.stdin.readline

S = input().strip()
q = int(input()) ### 질문의 수 1 <= q <= 200,000
a_zArr = [[0 for i in range(26)] for i in range(len(S))]
a_zArr[0][ord(S[0]) - 97] = 1
for i in range(1, len(S)):
    a_zArr[i][ord(S[i]) - 97] = 1
    for j in range(26):
        a_zArr[i][j] += a_zArr[i - 1][j]

for i in range(q):
    a, l, r = input().strip().split()
    l = int(l)
    r = int(r)
    if l > 0:
        res = a_zArr[r][ord(a[0]) - 97] - a_zArr[l - 1][ord(a[0]) - 97]
    else:
        res = a_zArr[r][ord(a[0]) - 97]
    print(res)
# import sys
# import math
# input = sys.stdin.readline

# N = input().strip()
# N = N.replace('9', '6')
# count = dict()

# for i in N:
#     count[i] = count.get(i, 0)
#     if i == '6':
#         count[i] += 0.5
#     else:
#         count[i] += 1

# count = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
# if list(count.keys())[0] == '6':
#     print(math.ceil(list(count.values())[0]))
# else:
#     print(list(count.values())[0])


# 제일 좋은 풀이
word = input().strip()
ans = [0] * 10
for i in range(len(word)):
    num = int(word[i])
    if num == 6 or num == 9:
        if ans[6] <= ans[9]:
            ans[6] += 1
        else:
            ans[9] += 1
    else:
        ans[num] += 1

print(max(ans))

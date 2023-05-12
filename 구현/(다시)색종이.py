N = int(input())
paper = [[0] * 101 for _ in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            paper[i][j] = 1  # 해당 범위를 1로 변환

answer = 0
for row in paper:
    answer += row.count(1)  # 덮은 색종이 범위를 계산
print(answer)

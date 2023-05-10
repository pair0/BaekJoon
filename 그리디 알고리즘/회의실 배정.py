import sys

N = int(sys.stdin.readline())
time = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = 0
sorti = 0

time.sort()
time.sort(key=lambda x: x[1])

for i in range(len(time)):
    if sorti <= time[i][0]:  # 다음 회의 시작시간이 이전 회의 끝나는 시간 이후일 시
        sorti = time[i][1]  # 끝나는 저장
        count += 1

print(count)

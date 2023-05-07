import  sys

N = int(sys.stdin.readline())
time = [0] * N
count = 1

for i in range(N):
    time[i] = list(map(int, sys.stdin.readline().strip().split(" ")))

time.sort(key=lambda x:x[1])
print(time)
for i in range(1, len(time)):
    if time[0][1] <= time[i][0]: ## 다음 회의 시작시간이 이전 회의 끝나는 시간 이후일 시
        time[0][1] = time[i][1] ## 끝나는 저장
        count += 1

print(count)
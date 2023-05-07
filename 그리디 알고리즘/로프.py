import sys

N = int(sys.stdin.readline())
loop_max = list()

for i in range(N):
    loop_max.append(int(sys.stdin.readline().strip()))

loop_max.sort(reverse=True)

for i in range(len(loop_max)):
    if loop_max[0] < (loop_max[i]*(i+1)):
        loop_max[0] = (loop_max[i]*(i+1)) ##병렬로 연결한 로프가 중량을 더 많이 달 수 있으면 list[0]의 저장

print(loop_max[0])
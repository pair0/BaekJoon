import sys

N = int(sys.stdin.readline())

for i in range(N):
    cloth_hash = {}
    answer = 1
    for j in range(int(sys.stdin.readline())):
        key, value = sys.stdin.readline().strip().split(" ")
        if cloth_hash.get(value): ##등록된 옷이면 +1을 해준다.
            cloth_hash[value] += 1
        else: ##등록되지 않은 옷이면 2로 저장 => 옷을 입지 않은 경우에 수까지 포함하기 때문에 2로 저장
            cloth_hash[value] = 2
    for value in cloth_hash.values(): ## .values() : dict의 value 값들만 저장
        answer *= value
    print(answer - 1) ## 옷을 전부 입지 않은 경우의 수를 빼준다.

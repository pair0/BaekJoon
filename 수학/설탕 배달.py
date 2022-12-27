import sys

N = int(sys.stdin.readline())
result = 0

while N >= 0:
    if N % 5 == 0: ## 섵탕 무게가 5의 배수가 되면 실행
        result += N//5 
        print(result) ##총 합을 출력
        break
    N -= 3 ##설탕 무게가 5의 배수가 될 때까지 3키로씩 줄인다.
    result += 1 ##3키로씩 줄일때 마다 가방 +1
else:
    print("-1")

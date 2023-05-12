import sys
input = sys.stdin.readline

A, B = map(int, input().split())
answer = 1

# top-down 방식으로 푼다. (bfs로는 bottom-up으로 풀 수 있다.)
while A != B:
    answer += 1
    temp = B
    if B % 10 == 1:  # B를 10으로 나눈 나머지가 1이면 A 오른쪽에 1을 붙일 수 있는 것이므로
        B //= 10  # B를 10으로 나눈 몫을 B에 저장
    elif B % 2 == 0:  # B를 2로 나눈 나머지가 0이면 A에 2를 곱할 수 있는 것이므로
        B //= 2  # B를 2로 나눈 몫을 저장

    if temp == B:  # 위에 연산 두개 중 어떤 것도 수행을 하지 못하였으면 A에서 B로 변환하지 못하므로
        answer = -1  # 결과에 -1 저장
        break

print(answer)

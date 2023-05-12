import sys
input = sys.stdin.readline

M = int(input())
S = set()  # 집합 자료형으로 변경

for _ in range(M):
    operate = input().split()
    if len(operate) == 1:
        if operate[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    else:
        oper, num = operate[0], operate[1]
        num = int(num)

        if oper == "add":
            S.add(num)  # set 자료형에서는 중복된 원소를 허용하지 않으므로 중복 체크를 할 필요 없음
        elif oper == "remove":
            S.discard(num)  # 집합에서 해당 원소가 없는 경우에도 오류가 발생하지 않음
        elif oper == "check":
            if num in S:
                print(1)
            else:
                print(0)
        elif oper == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)

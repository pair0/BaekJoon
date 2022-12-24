def solution(p_list):
    count = 0
    answer = []
    for type in p_list:
        hash_map[type] = hash_map.get(type, 0) + 1

    for type, value in hash_map.items():  ##for key, value in hash_map.items():는 딕셔너리 hash_map에서 키-값 쌍을 꺼내서 키는 key에 값은 value에 저장하고, 꺼낼 때마다 코드를 반복합니다.
        if value > 1:
            count += 1
            answer.append(type)

    print(count)
    for i in sorted(answer):
        print(i)


N, M = map(int, input().split())
p_list = []
hash_map = {}


for i in range(N+M):
    p_list.append(input())


solution(p_list)
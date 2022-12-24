def solution(card, card_num):
    hash_map = {}
    for type in card:
        hash_map[type] = hash_map.get(type, 0) + 1 #각 키마다 갯수 파악

    for i in card_num:
        if i not in hash_map:
            print(0, end=" ")
        else:
            print(hash_map[i], end=" ")


N = int(input())
card = list(map(int, input().split()))
M = int(input())
card_num = list(map(int, input().split()))

solution(card, card_num)
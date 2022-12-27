import sys

def Cycle(N):
    N_list = list(N)
    if int(N) < 10:
        N_list.insert(0, 0)
    return N_list


N = sys.stdin.readline().strip()

result = 0
count = 0

N_list = Cycle(N)

while True:
    result = int(N_list[0]) + int(N_list[1])
    count += 1

    N_list[0] = N_list[1]
    N_list[1] = Cycle(str(result))[1]

    result = ''.join(map(str, N_list))
    if int(N) == int(result):
        break

print(count)
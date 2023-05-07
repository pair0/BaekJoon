import sys
N = int(sys.stdin.readline())
one_number_count = 99

if N < 100:
    print(N)
else:
    for i in range(100, N+1):
        choose = str(i)
        X = set()
        for j in range(len(choose)-1):
            X.add(int(choose[j]) - int(choose[j+1]))
        if len(X) == 1:
            one_number_count += 1
    print(one_number_count)




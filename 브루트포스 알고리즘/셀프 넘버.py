num = set(range(1, 10000+1))
create_number = set()

for i in num:
    for j in str(i):
        i += int(j)
    create_number.add(i)

self_number = num - create_number
for i in sorted(self_number):
    print(i)
from re import T


t = int(input())

while(t > 0):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dx = x1 - x1
    dy = y1 - y2
    
    if(r1 > r2):
        r1, r2 = r2, r1
    add = r1 + r2
    add = add * add
    sub = r2 - r1
    sub = sub * sub
    d = dx*dx + dy*dy

    if(d < add and d > sub):
        print("2")
    elif(d == add or (d == sub and d != 0)):
        print("1")
    elif(d < sub or d > add):
        print("0")
    elif(d == 0):
        if(r1 == r2):
            print("-1")
        else:
            print("0")
    t -= 1


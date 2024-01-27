n = int(input())
area =0
if n==1:
    print(area)
else:
    l=[]
    for _ in range(n):
        l.append(list(map(int,input().split())))
    maxx=l[0][0]
    minx=l[0][0]
    maxy=l[0][1]
    miny=l[0][1]
    for __ in range(n):
        if minx>l[__][0]:
            minx=l[__][0]
        if maxx<l[__][0]:
            maxx=l[__][0]
        if miny>l[__][1]:
            miny=l[__][1]
        if maxy<l[__][1]:
            maxy=l[__][1]
    area=(maxx-minx)*(maxy-miny)
    print(area)    
    
import sys
input = sys.stdin.readline

n,m,b = map(int,input().strip().split())
ground =[list(map(int,input().split())) for _ in range(n)]
minn=257
maxx=0
for _ in range(n):
    minn =min(minn,min(ground[_]))
    maxx=max(maxx,max(ground[_]))
time_min=500*500*2*257
height_max=0
for height in range(minn,maxx+1):
    t=0
    box =b
    for row in range(n):
        for col in range(m):
            present = ground[row][col]
            if present>=height:
                t +=(present-height)*2
                box +=(present-height)
            else:
                t +=(height-present)
                box -=(height-present)
    if box>=0 and time_min>t:
        time_min=t
        height_max=height
    elif box>=0 and time_min==t and height_max<height:
        height_max=height
print(time_min,height_max)
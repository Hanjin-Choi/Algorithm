import sys,collections
input = sys.stdin.readline

n,m,b = map(int,input().strip().split())
ground =[]
for _ in range(n):
    ground+=list(map(int,input().split()))
minn=min(ground)
maxx=max(ground)

num = collections.Counter(ground)

time_min=500*500*2*257
height_max=0
for height in range(minn,maxx+1):
    t=0
    box =b
    for present, c in num.items():
        if present>=height:
            t+=(present-height)*c*2
            box+=(present-height)*c
        else:
            t+=(height-present)*c
            box-=(height-present)*c
    if box>=0 and time_min>t:
        time_min=t
        height_max=height
    elif box>=0 and time_min==t and height_max<height:
        height_max=height
    elif box<0:
        break
print(time_min,height_max)
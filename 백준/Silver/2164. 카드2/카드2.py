import sys
input = sys.stdin.readline
#
n = int(input())
l= [2*x for x in range(1,n//2+1)]
if n==1:
    print(1)
else:
    if n %2 ==0:
        discard = n//2
        motion = 0
    else:
        discard = n//2+1
        motion=1
    idx = 0
    while discard < n-1:
        if l[idx]:
            if motion % 2 ==0:
                l[idx]=0
                discard +=1
            motion +=1
        idx+=1
        if idx ==n//2:
            idx =0
    print(max(l))
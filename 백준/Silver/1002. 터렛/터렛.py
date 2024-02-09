import sys
input = sys.stdin.readline

t= int(input())
for tc in range(t):
    l=list(map(int,input().split()))
    distance = ((l[0]-l[3])**2 + (l[1]-l[4])**2)**0.5
    r1 = l[2]
    r2 = l[5]
    if distance > r1+r2:
        print(0)
    elif distance == r1 +r2:
        print(1)
    elif distance==0 and r1==r2:
        print(-1)
    elif distance == abs(r2-r1):
        print(1)
    elif abs(r1-r2) <distance< r1+r2:
        print(2)
    else:
        print(0)

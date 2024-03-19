import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    s,e=map(int,input().split())
    n=e-s
    x=int(n**0.5)
    if (x-1)**2+(x-1)>=n:
        print(2*(x-1))
    elif (x-1)**2+2*x-1>=n:
        print(2*x-1)
    elif x**2+x>=n:
        print(2*x)
    else:
        print(2*x+1)
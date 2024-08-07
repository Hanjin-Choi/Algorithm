import sys
input = sys.stdin.readline
from collections import deque
n=int(input())
q=deque()
for _ in range(n):
    l=input().strip()
    num= int(l[0])
    if num==1:
        a,b=map(int,l.split())
        q.appendleft(b)
    elif num==2:
        a, b = map(int, l.split())
        q.append(b)
    elif num==3:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif num==4:
        if q:
            print(q.pop())
        else:
            print(-1)
    elif num==5:
        print(len(q))
    elif num==6:
        if q:
            print(0)
        else:
            print(1)
    elif num==7:
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)
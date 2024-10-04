import sys
from collections import deque
input=sys.stdin.readline

n,k,m = map(int,input().split())
q=deque([i for i in range(1,n+1)])
cnt=0
while q:
    if (cnt//m)%2:
        q.rotate(k)
    else:
        q.rotate(1-k)
    print(q.popleft())
    cnt +=1

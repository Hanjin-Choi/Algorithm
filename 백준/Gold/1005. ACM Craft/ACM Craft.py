import sys
input = sys.stdin.readline
from collections import deque

t=int(input())
for tc in range(t):
    n,k = map(int,input().split())
    lst =[0]+ list(map(int,input().split()))
    adjl = [[] for v in range(n+1)]
    res =lst[:]
    head =set()
    tail =set()
    num_head = [0]*(n+1)
    for _ in range(k):
        x,y = map(int,input().split())
        adjl[x].append(y)
        head.add(x)
        tail.add(y)
        num_head[y] += 1
    candidate = head-tail
    target= int(input())
    q=deque()
    for root in candidate:
        q.append(root)
    while q:
        now = q.popleft()
        for go in adjl[now]:
            res[go] = max(res[go],res[now]+lst[go])
            num_head[go]-=1
            if not num_head[go]:
                q.append(go)
    print(res[target])
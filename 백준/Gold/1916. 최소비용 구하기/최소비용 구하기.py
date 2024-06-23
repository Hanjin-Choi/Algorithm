import sys
input = sys.stdin.readline
from heapq import heappop,heappush
n=int(input())
m=int(input())

adjl=[[] for _ in range(n+1)]
for _ in range(m):
    s,e,c =map(int,input().split())
    adjl[s].append([c,e])
start,end=map(int,input().split())
dijk = [float('inf')]*(n+1)
dijk[start]=0
pq=[(0,start)]
while pq:
    dist, now=heappop(pq)
    if dijk[now]<dist:
        continue
    for plus, to in adjl[now]:
        new = plus + dist
        if new >= dijk[to]:
            continue
        dijk[to]=new
        heappush(pq,(new,to))
print(dijk[end])
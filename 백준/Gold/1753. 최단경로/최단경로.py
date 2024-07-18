import sys
input = sys.stdin.readline
from heapq import heappop, heappush
v,e = map(int,input().split())
k=int(input())
res= [float('INF')]*(v+1)
res[k]=0
adjl=[[] for _ in range(v+1)]
for _ in range(e):
    f,t,w = map(int,input().split())
    adjl[f].append((w,t))
pq=[(0,k)]
while pq:
    dist, p = heappop(pq)
    if res[p]<dist:continue
    for to in adjl[p]:
        if dist+to[0]<res[to[1]]:
            res[to[1]]=dist+to[0]
            heappush(pq,(dist+to[0],to[1]))
for i in range(1,v+1):
    if res[i]==float('inf'):
        print('INF')
    else:
        print(res[i])
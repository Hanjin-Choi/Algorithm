from heapq import heappop,heappush
import sys
input = sys.stdin.readline

n,d =map(int,input().split())
dist=[float('inf')]*(d+1)
graph = [[(i+1,1)] for i in range(d)]
for idx in range(n):
    s,e,dis=map(int,input().strip().split())
    t=e-s-dis
    if t>0 and e<=d:
        graph[s].append((e,dis))

pq=[(0,0)]
dist[0]=0
while pq:
    cost, now=heappop(pq)
    for end,distance in graph[now]:
        total = cost + distance
        if dist[end]<total:continue
        dist[end]=total
        if end !=d:
            heappush(pq,(total,end))
print(dist[d])
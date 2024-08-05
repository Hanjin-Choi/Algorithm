import sys
input = sys.stdin.readline
from heapq import heappop,heappush

n,e = map(int,input().split())
adjl=[[] for _ in range(n+1)]
res=[[float('inf')]*(n+1) for _ in range(5)]
def dijkstra(x,y,i):
    pq=[]
    heappush(pq,(0,x))
    res[i][x]=0
    while pq:
        dist,now = heappop(pq)
        if now ==y:break
        if res[i][now] < dist:
            continue
        for forward,arrive in adjl[now]:
            if dist+forward >=res[i][arrive]:
                continue
            res[i][arrive]=dist+forward
            heappush(pq,(res[i][arrive],arrive))

for _ in range(e):
    a,b,c=map(int,input().split())
    adjl[a].append((c,b))
    adjl[b].append((c,a))
v1,v2 = map(int,input().split())
dijkstra(1,v1,0)
d1=res[0][v1]
dijkstra(n,v2,1)
d2=res[1][v2]
dijkstra(1,v2,2)
d3=res[2][v2]
dijkstra(n,v1,3)
d4=res[3][v1]
dijkstra(v1,v2,4)
d5=res[4][v2]
ans = min(d1+d2,d3+d4)+d5
if ans==float('inf'):
    print(-1)
else:
    print(ans)
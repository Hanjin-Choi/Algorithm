import sys
input = sys.stdin.readline
from heapq import heappop,heappush

n,k = map(int,input().split())
visit=[float('inf')]*(100001)
pq = [(0,n)]
while pq:
    c,now = heappop(pq)
    visit[now]=c
    if now==k:
        break
    if now-1>=0 and visit[now-1]>c+1:
        heappush(pq,(c+1,now-1))
    if now +1<=100000 and visit[now+1]>c+1:
        heappush(pq,(c+1,now+1))
    if now*2<=100000 and visit[now*2]>c:
        heappush(pq,(c,now*2))
print(visit[k])
import sys
input = sys.stdin.readline
from heapq import heappush,heappop

n,k = map(int,input().split())
jewel =[list(map(int,input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
jewel.sort()
bag.sort()
pq =[]
idx=0
ans=0
for b in bag:
    while idx<n and jewel[idx][0]<= b:
        heappush(pq,-jewel[idx][1])
        idx+=1
    if pq:
        v=heappop(pq)
        ans -=v
print(ans)
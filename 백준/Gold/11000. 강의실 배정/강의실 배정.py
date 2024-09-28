import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n=int(input())
lst =[]

cnt=1
for i in range(n):
    s,t= map(int,input().split())
    lst.append((s,t))
lst.sort(key=lambda x:(x[0],x[1]))

pq=[lst[0][1]]
for s,t in lst[1:]:
    if pq[0] <= s:
        heappop(pq)
    heappush(pq,t)
print(len(pq))
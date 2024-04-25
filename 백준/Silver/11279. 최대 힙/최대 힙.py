import sys
from heapq import heappush,heappop
input = sys.stdin.readline

n=int(input())
mxheap=[]
for _ in range(n):
    x = int(input())
    if x:
        heappush(mxheap,-x)
    elif mxheap:
        print(-heappop(mxheap))
    else:
        print(0)

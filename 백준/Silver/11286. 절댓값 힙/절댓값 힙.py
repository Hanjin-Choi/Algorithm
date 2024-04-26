import sys
input = sys.stdin.readline
from heapq import heappush,heappop
n =int(input())
heap =[]
for _ in range(n):
    x =int(input())
    if not x and heap:
        num, ab = heappop(heap)
        print(num*ab)
    elif not x and not heap:
        print(0)
    elif x>0:
        heappush(heap,(x,1))
    else:
        heappush(heap,(-x,-1))
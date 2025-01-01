from heapq import heapify, heappop
n,k=map(int,input().split())
lst= list(map(int,input().split()))

heapify(lst)
for i in range(k-1):
    heappop(lst)
print(heappop(lst))
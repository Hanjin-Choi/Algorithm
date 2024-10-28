from heapq import heappop,heappush
n=int(input())
k=int(input())
lst= list(map(int,input().split()))

lst.sort()
pq=[]
for i in range(1,n):
    heappush(pq,lst[i-1]-lst[i])
for _ in range(min(k-1,n-1)):
    heappop(pq)
ans=0
while pq:
    ans-=heappop(pq)
print(ans)
from heapq import heappop,heappush
n=int(input())
lst=[]
idx=1
da=int(input())
ans=0
for a in range(n-1):
    v=int(input())
    heappush(lst,-v)
while lst and -lst[0]>=da:
    temp = -heappop(lst)
    da+=1
    ans+=1
    if temp>=1:
        heappush(lst,-(temp-1))
print(ans)
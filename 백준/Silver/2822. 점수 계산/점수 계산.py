from heapq import heappop,heappush
pq =[]
for i in range(1,9):
    num = int(input())
    heappush(pq,(-num,i))
ans=[]
cnt=0
for _ in range(5):
    score,i=heappop(pq)
    cnt -=score
    ans.append(i)
ans.sort()
print(cnt)
print(*ans)
   
    
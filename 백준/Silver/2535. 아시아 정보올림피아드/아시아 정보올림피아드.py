from heapq import heappop,heappush
n=int(input())
pq= []
medal=[]
for _ in range(n):
    nation, num, score = map(int,input().split())
    heappush(pq,(-score,nation,num))
for i in range(2):
    score, nation,num = heappop(pq)
    medal.append((nation,num))
if medal[0][0]!=medal[1][0]:
    score, nation,num = heappop(pq)
    medal.append((nation, num))
else:
    while pq[0][1]==medal[0][0]:
        heappop(pq)
    score, nation, num = heappop(pq)
    medal.append((nation, num))
for i in range(3):
    print(*medal[i])



import sys
input = sys.stdin.readline
from heapq import heappop,heappush
n,k,m = map(int,input().split())
price = [[_]+list(map(int,input().split())) for _ in range(n)]
price.sort(key=lambda x: x[2])
visit=[0]*n
pq =[]
total=0
for i in range(k):
    idx,p,c = price[i]
    if m >=c:
        heappush(pq,(p-c,p,c))
        m-=c
        total +=1
        visit[idx]=1
    else:
        break
if pq:
    price.sort(key=lambda x:x[1])
    for i in range(n):
        if visit[price[i][0]]:
            continue
        prior, p,c = heappop(pq)
        if c+ price[i][1]<=p+price[i][2] and price[i][1]<=m:
            m-=price[i][1]
            total +=1
            heappush(pq,(prior,p,c))
        elif c+price[i][1]>price[i][2]+p and m+c>= price[i][2]+p:
            m+=c-price[i][2]-p
            total +=1
            heappush(pq,(price[i][1]-price[i][2],price[i][1],price[i][2]))
        elif m>=price[i][1]:
            m-=price[i][1]
            heappush(pq,(prior,p,c))
        else:
            heappush(pq, (prior, p, c))
print(total)

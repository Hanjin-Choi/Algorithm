import sys
input = sys.stdin.readline
from heapq import heappop,heappush

def find_set(i):
    if p[i]==i:
        return i
    else:
        p[i]=find_set(p[i])
        return p[i]

def union(x,y):
    x=find_set(x)
    y=find_set(y)
    if x==y:
        return
    if x<y:
        p[y]=x
    else:
        p[x]=y


v,e = map(int,input().split())
cnt=0
pq=[]
weight=0
p=[i for i in range(v+1)]

for _ in range(e):
    a,b,c =map(int,input().split())
    heappush(pq,(c,a,b))

while pq:
    w,s,e = heappop(pq)
    if find_set(s)==find_set(e):
        continue
    union(s,e)
    weight +=w
    cnt +=1
    if cnt ==v-1:
        break
print(weight)
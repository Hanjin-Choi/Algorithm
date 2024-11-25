from heapq import heappop,heappush
r,c = map(int,input().split())

arr= [input() for _ in range(r)]
ans =[0]*10
pq=[]
for i in range(r):
    cnt=0
    for idx in range(c):
        if arr[i][idx]=='.':
            cnt+=1
        elif arr[i][idx].isnumeric():
            ans[int(arr[i][idx])]=cnt
for i in range(1,10):
    heappush(pq,(-ans[i],i))
prize=1
while pq:
    score,num = heappop(pq)
    ans[num]=prize
    if pq and score!=pq[0][0]:
        prize+=1
for i in range(1,10):
    print(ans[i])
n,score,p=map(int,input().split())
if n!=0:
    lst=list(map(int,input().split()))
cnt=0
m=100
d={}
d[score]=1
for idx in range(n):
    if lst[idx]>score:
        cnt+=1
    if lst[idx]<m:
        m=lst[idx]
    if lst[idx] in d:
        d[lst[idx]]+=1
    else:
        d[lst[idx]]=1
    
cnt+=d[score]
if cnt>p:
    print(-1)
else:
    print(cnt+1-d[score])
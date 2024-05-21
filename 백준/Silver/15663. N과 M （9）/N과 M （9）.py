def per(i):
    if i==m:
        res.add(tuple(ans))
    else:
        for j in range(n):
            if not visit[j]:
                visit[j]=1
                ans[i]=lst[j]
                per(i+1)
                visit[j]=0
n,m = map(int,input().split())
lst = list(map(int,input().split()))
res = set()
ans=[0]*m
visit = [0]*n
per(0)
res=list(res)
res.sort()
for i in res:
    print(*i)
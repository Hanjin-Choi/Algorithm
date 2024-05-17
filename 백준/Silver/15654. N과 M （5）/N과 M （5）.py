def per(i):
    if i==m:

        print(*ans)
    else:
        for j in range(n):
            if not visit[j]:
                visit[j]=1
                ans[i]=lst[j]
                per(i+1)
                visit[j]=0


n,m =map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
visit=[0]*n
ans=[0]*m
per(0)
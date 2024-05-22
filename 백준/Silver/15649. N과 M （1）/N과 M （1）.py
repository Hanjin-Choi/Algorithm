def back(c):
    if c==m:
        print(*ans)
    else:
        for i in range(n):
            if not visit[i]:
                visit[i]=1
                ans[c]=i+1
                back(c+1)
                visit[i]=0

n,m=map(int,input().split())
ans=[0]*m
visit=[0]*n
back(0)
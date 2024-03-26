def back(k,c):
    if m==c:
        res=[]
        for i in range(n):
            if visit[i]:
                res.append(num[i])
        print(*res)
    elif k==n:
        return
    else:
        visit[k]=1
        back(k+1,c+1)
        visit[k]=0
        back(k+1,c)

n,m=map(int,input().split())
num=[i for i in range(1,n+1)]
visit=[0]*n
back(0,0)
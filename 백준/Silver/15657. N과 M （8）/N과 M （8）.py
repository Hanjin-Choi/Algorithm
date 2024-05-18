def back(i,c):
    if c==m:
        print(*ans)
    else:
        for j in range(i,n):
            ans[c]=lst[j]
            back(j,c+1)

n,m =map(int,input().split())
lst = list(map(int,input().split()))
lst.sort()
ans = [0]*m
back(0,0)
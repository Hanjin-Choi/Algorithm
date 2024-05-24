def back(i,k):
    if i ==m:
        print(*ans)
    else:
        for j in range(k,n):
            ans[i]=lst[j]
            back(i+1,j)

n,m = map(int,input().split())
lst = set(map(int,input().split()))
lst =list(lst)
lst.sort()
n =len(lst)
ans=[0]*m
back(0,0)

def dfs(n):
    if n in d:
        return d[n]
    else:
        a = dfs(n//p)
        b= dfs(n//q)
        d[n]=a+b
        return d[n]




n,p,q =map(int,input().split())
d={0:1,1:2}
print(dfs(n))
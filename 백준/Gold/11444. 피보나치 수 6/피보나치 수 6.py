def dfs(x):
    if x<=2:
        return fib[x]
    elif x in fib:
        return fib[x]
    elif x%2:
        a=dfs((x+1)//2)
        b=dfs(x//2)
        fib[x]=((a) ** 2 + (b ** 2)) % 1000000007
        return fib[x]
    else:
        c=dfs(x//2)
        d=dfs(x//2-1)
        fib[x]=(c**2+2*c*d)%1000000007
        return fib[x]


n=int(input())
fib={0:0,1:1,2:1}
ans=dfs(n)
print(ans)
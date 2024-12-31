def comb(n,c):
    if c>n-c:
        c = n-c
    res=1

    for i in range(c):
        res*=(n-i)
        res//=(i+1)
    return res

n,c = map(int,input().split())
print(comb(n,c))

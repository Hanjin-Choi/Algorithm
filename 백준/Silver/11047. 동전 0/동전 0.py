n,k = map(int,input().split())
won = [int(input()) for _ in range(n)]
ans=0
for i in range(n-1,-1,-1):
    if k:
        d,m= divmod(k,won[i])
        k-=d*won[i]
        ans +=d
    else:
        break
print(ans)
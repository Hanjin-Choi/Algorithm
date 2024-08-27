n=int(input())
ans=1
for i in range(n):
    ans *=(10+i)
    ans //=(i+1)
ans %=10007
print(ans)
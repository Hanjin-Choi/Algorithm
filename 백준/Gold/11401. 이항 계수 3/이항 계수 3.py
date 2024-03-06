def mul(a,i):
    if i==1:
        return a
    if i%2:
        res = mul(a,i//2)**2*a
        if res>=1000000007:
            return res%1000000007
        else:
            return res
    else:
        res = mul(a,i//2)**2
        if res >= 1000000007:
            return res % 1000000007
        else:
            return res

n,k = map(int,input().split())
if k < n-k:
    k=n-k
ans =1
for i in range(n-k):
    ans *= ((n-i)*mul(i+1,1000000005))
    ans%=1000000007

print(ans)


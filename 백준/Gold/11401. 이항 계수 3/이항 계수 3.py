def fact(n):
    f=1
    for i in range(2,n+1):
        f =(f*i)%1000000007
    return f
def modd(num,i):
    if i ==1:
        return num
    if i%2:
        return (modd(num,i//2)**2*num) % 1000000007
    else:
        return (modd(num,i//2)**2) % 1000000007
n,k = map(int,input().split())
if k<n-k:
    k=n-k
ja = 1
mo=fact(n-k)
for i in range(n-k):
    ja=(ja*(n-i))%1000000007
print((modd(mo,1000000005)*ja)%1000000007)
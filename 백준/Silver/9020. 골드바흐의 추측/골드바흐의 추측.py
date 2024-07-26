sosu = [1]*10001
num=set()
for i in range(2,10001):
    if sosu[i]:
        num.add(i)
        for j in range(i*2,10001,i):
            sosu[j]=0

t=int(input())
for _ in range(t):
    n=int(input())
    for k in num:
        if k<=n//2 and n-k in num:
            ans=[k,n-k]
    print(*ans)
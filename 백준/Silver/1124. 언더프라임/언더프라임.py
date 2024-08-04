import sys
input = sys.stdin.readline
prime=[]
flag=[0]*(int(100000**0.5) +1)
res=[0]*(int(100000**0.5) +1)

for i in range(2,int(100000**0.5) +1):
    if not flag[i]:
        prime.append(i)
        res[i]=1
        for j in range(2*i,int(100000**0.5) +1,i):
            flag[j]=1
s=set(prime)
def p(x):
    cnt=0
    for p in prime:
        if p>x:break
        while x%p==0:
            cnt+=1
            x//=p
    if x !=1:
        cnt+=1
    if cnt in s:
        return 1
    else: return 0

a,b = map(int,input().split())
ans=0
for x in range(a,b+1):
    ans+=p(x)
print(ans)

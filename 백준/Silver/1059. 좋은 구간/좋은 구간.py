l=int(input())
s=list(map(int,input().split()))
n=int(input())
s.sort()
idx=0
ans=0
while s[idx]<n:
    idx +=1
if s[idx]==n:
    pass
else:
    if idx==0:
        start=1
    else:
        start = s[idx-1]+1
    end=s[idx]-1
    ans = (n-start)*(end-n+1) + end-n

print(ans)
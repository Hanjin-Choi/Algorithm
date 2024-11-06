n=int(input())
lst =[int(input()) for _ in range(n)]

lst.sort()

ans=5
for i in range(n):
    cnt=0
    for j in range(lst[i],lst[i]+5):
        if j not in lst:
            cnt+=1
    ans=min(ans,cnt)
print(ans)
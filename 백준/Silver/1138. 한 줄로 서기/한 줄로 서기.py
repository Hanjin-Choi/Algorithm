
n= int(input())
lst=list(map(int,input().split()))
ans=[]
for i in range(n-1,-1,-1):
    ans.insert(lst[i],i+1)
print(*ans)
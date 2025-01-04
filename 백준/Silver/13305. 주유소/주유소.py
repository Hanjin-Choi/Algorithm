n=int(input())
di = list(map(int,input().split()))
cost = list(map(int,input().split()))
ans=di[n-2] * cost[n-2]
dist=di[n-2]
for i in range(1,n-1):
    if dist * cost[n-2-i]<ans:
        dist += di[n-2-i]
        ans = dist * cost[n-2-i]
    else:
        dist += di[n-2-i]
        ans += di[n-2-i]*cost[n-2-i]
print(ans)
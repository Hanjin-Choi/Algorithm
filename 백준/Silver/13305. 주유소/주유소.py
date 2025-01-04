n=int(input())
di = list(map(int,input().split()))
cost = list(map(int,input().split()))
ans=0
co=cost[0]
dist=di[0]
for i in range(1,n-1):
    if co<cost[i] :
        dist += di[i]
    else:
        ans += dist*co
        dist = di[i]
        co=cost[i]
ans += dist*co
print(ans)
n=int(input())

lst = [list(map(int,input().split())) for _ in range(n)]
res= [0]*(n+1)
for i in range(n):
    date = lst[i][0] + i
    res[i+1]=max(res[i],res[i+1])
    if date <=n:
        res[date]=max(lst[i][1]+res[i],res[date])
print(res[n])
n=int(input())
lst=list(map(int,input().split()))

d={i:0 for i in range(51)}
for num in lst:
    d[num] +=1
res=[]
for i in range(51):
    if i==d[i]:
        res.append(i)
if res:
    res.sort(reverse=True)
    print(res[0])
else:
    print(-1)

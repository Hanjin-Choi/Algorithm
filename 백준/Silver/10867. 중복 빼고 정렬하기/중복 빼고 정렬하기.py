n=int(input())
lst= list(map(int,input().split()))
res =[0]*2001
for i in lst:
    res[i]+=1

for idx in range(-1000,1001):
    if res[idx]:
        print(idx,end=' ')
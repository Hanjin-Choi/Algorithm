n=int(input())
res=[0]*3
res[1]=1
res[2]=2
for i in range(3,n+1):
    res[i%3]=(res[(i-1)%3] +res[(i-2)%3])%15746
print(res[n%3])
res=[0]*100001
res[1]=3
res[2]=7
n=int(input())
for i in range(3,n+1):
    res[i]=(2*res[i-1]+res[i-2])%9901
print(res[n])
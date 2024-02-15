L=[]
while True:
    inp = int(input())
    if inp ==0:
        break
    else:
        L.append(inp)
n=max(L)
era=[0,0]+[1]*2*n
prime=[]
pcount=[0]*(2*n+2)
for i in range(2,2*n+2):
    pcount[i]+=pcount[i-1]
    if era[i]:
        pcount[i]+=1
        for j in range(2*i,n*2+1,i):
            era[j]=0
for j in L:
    ans=pcount[2*j]-pcount[j]
    print(ans)
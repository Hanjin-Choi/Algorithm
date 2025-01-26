l=int(input())
d=int(input())
x=int(input())
di={i:[] for i in range(37)}
for i in range(l,d+1):
    num=i
    s=0
    for j in range(5):
        s+=num%10
        num//=10
    di[s].append(i)
print(di[x][0])
print(di[x][-1])
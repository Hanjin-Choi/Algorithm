bi=[0,0,0,0,0,0,0,0]
x=int(input())
for i in range(7):
    x,m=divmod(x,2)
    bi[i]=m
print(sum(bi))


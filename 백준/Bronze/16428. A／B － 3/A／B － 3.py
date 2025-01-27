a,b=map(int,input().split())

m,r=divmod(a,b)
if r<0:
    m+=1
    r+=abs(b)
print(m)
print(r)
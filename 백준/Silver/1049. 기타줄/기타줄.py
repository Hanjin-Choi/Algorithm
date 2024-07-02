import math
n,m=map(int,input().split())
pack=[]
one=[]
for _ in range(m):
    p,o = map(int,input().split())
    pack.append(p)
    one.append(o)
pack.sort()
one.sort()
tar=one[0]*n
tar=min(tar,n//6*pack[0]+n%6*one[0],math.ceil(n/6)*pack[0])
print(tar)
import math
A,B,V=map(int,input().split())
c=1+math.ceil((V-A)/(A-B))
print(c)
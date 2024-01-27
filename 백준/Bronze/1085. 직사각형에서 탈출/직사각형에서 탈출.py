x,y,w,h = map(int,input().split())
l = x
r = w-x
u = h-y
d = y
print(min(l,r,u,d))
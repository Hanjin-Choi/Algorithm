import sys
a,b = map(int,sys.stdin.readline().split())
c,d = map(int,sys.stdin.readline().split())

ja = a*d + b*c
mo = b*d
max_mj = max(ja,mo)
min_mj = min(ja,mo)
r=1
while r !=0:
    d,r = divmod(max_mj,min_mj)
    max_mj, min_mj = min_mj, r
print(ja//max_mj,mo//max_mj)
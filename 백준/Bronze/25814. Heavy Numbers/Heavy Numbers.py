a,b = input().split()
lena=len(a)
lenb=len(b)
cala= lena*sum(list(map(int,a)))
calb= lenb*sum(list(map(int,b)))
if cala==calb:
    print(0)
elif cala>calb:
    print(1)
else:
    print(2)
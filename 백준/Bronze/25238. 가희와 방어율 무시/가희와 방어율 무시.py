a,b = map(int,input().split())

dam= a *(100-b)/100
if dam <100:
    print(1)
else:
    print(0)
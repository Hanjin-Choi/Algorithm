a,b = map(int,input().split())
s= a**2-b
if a**2-b==0:
    print(int((-a-s**0.5)))
else:
    print(int((-a-s**0.5)),int((-a+s**0.5)))
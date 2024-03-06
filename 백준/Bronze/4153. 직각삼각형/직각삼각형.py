while True:
    a,b,c = map(int,input().split())
    if a==0:
        break
    if a>b:
        a,b = b,a
    if b>c:
        b,c = c,b
    if c**2==a**2+b**2:
        print('right')
    else:
        print('wrong')
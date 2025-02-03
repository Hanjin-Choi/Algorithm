while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    a-=b
    if a%2 and a>1:
        print((a-3)//2,1)
    elif a%2 and a==1:
        print(0,0)
    elif not a%2:
        print(a//2,0)

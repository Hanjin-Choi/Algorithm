t=int(input())
a=b=c=0
for _ in range(t):
    x,y,z= map(int,input().split())
    a+=x
    b+=y
    c+=z
    temp= min(a,b,c)
    if temp<30:
        print('NO')
    else:
        print(temp)
        a-=temp
        b-=temp
        c-=temp
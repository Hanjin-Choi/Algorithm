n=int(input())
lst=list(map(int,input().split()))
young=[]
sik=[]
for idx in range(n):
    y=m=1
    y+=(lst[idx]//30)
    y*=10
    m+=(lst[idx]//60)
    m*=15
    young.append(y)
    sik.append(m)
sm=sum(sik)
sy=sum(young)
if sm==sy:
    print('Y M',sm)
elif sm>sy:
    print('Y',sy)
else:
    print('M',sm)
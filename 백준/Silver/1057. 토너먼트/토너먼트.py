n,kim,lim = map(int,input().split())
cnt=0
while kim!=lim:
    if kim==0:
        cnt =-1
        break
    if lim==0:
        cnt =-1
        break
    if kim%2:
        kim+=1
    if lim%2:
        lim+=1
    kim /=2
    lim/=2
    cnt+=1
print(cnt)
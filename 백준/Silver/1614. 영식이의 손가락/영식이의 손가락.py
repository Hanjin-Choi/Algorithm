n=int(input())
m=int(input())
lst = [1,2,3,4,5,4,3,2]
if n==1 or n==5:
    ans = 8*m
    if n==5:
        ans +=4
else:
    d,r = divmod(m,2)
    ans = d*8
    if n==2:
        if r:
            ans += 7
        else:
            ans +=1
    elif n==3:
        if r:
            ans +=6
        else:
            ans+=2
    elif n==4:
        if r:
            ans+=5
        else:
            ans+=3
print(ans)
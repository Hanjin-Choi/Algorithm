from math import comb

n=int(input())
idx=1
arr=[0]*10
temp=[]
def combi(c,cnt,l,t):
    if c==cnt:
        a=0
        for i in range(9,-1,-1):
            if t>>i & 1:
                a+=i*10**(c-1)
                c-=1
            if c==0:break
        temp.append(a)
    elif l>9:
        return
    else:
        combi(c+1,cnt,l+1,t+(1<<l))
        combi(c,cnt,l+1,t)
if n>=2**10-1:
    print(-1)
else:
    while n>0:
        if n >= comb(10,idx) and idx<10:
            n-=comb(10,idx)
            idx+=1
        else:
            break
    combi(0, idx, 0, 0)
    temp.sort()
    print(temp[n])

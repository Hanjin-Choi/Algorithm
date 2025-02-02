l=list(input().split(' '))
l[0]=int(l[0])
l[2]=int(l[2])
l[4]=int(l[4])
res1=l[0]
res2=l[2]

if l[1]=='+':
    res1+=l[2]
elif l[1]=='-':
    res1-=l[2]
elif l[1]=='*':
    res1*=l[2]
elif l[1]=='/':
    if res1*l[2]<0:
        if res1<0:
            res1*=-1
            res1//=l[2]
            res1*=-1
        else:
            l[2]*=-1
            res1//=l[2]
            res1*=-1
    else:
        res1//=l[2]

if l[3] == '+':
    res1 += l[4]
elif l[3] == '-':
    res1 -= l[4]
elif l[3] == '*':
    res1 *= l[4]
elif l[3] == '/':
    if res1 *l[4]<0:
        if res1<0:
            res1*=-1
            res1 //=l[4]
            res1*=-1
        elif l[4]<0:
            l[4]*=-1
            res1//=l[4]
            res1*=-1

    else:
        res1 //= int(l[4])


if l[3] == '+':
    res2+=l[4]
elif l[3] == '-':
    res2 -= l[4]
elif l[3] == '*':
    res2 *= l[4]
elif l[3] == '/':
    if res2*l[4]<0:
        if res2<0:
            res2*=-1
            res2//=l[4]
            res2*=-1
        else:
            l[4]*=-1
            res2//=l[4]
            res2*=-1
    else:
        res2//=l[4]


if l[1] == '+':
    res2 += l[0]
elif l[1] == '-':
    res2 = l[0]-res2
elif l[1] == '*':
    res2 *=l[0]
elif l[1] == '/':
    if res2*l[0]<0:
        if res2<0:
            res2*=-1
            res2=l[0]//res2
            res2*=-1
        else:
            l[0]*=-1
            res2=l[0]//res2
            res2*=-1
    else:
        res2 = l[0] //res2
print(min(res1,res2))
print(max(res1,res2))
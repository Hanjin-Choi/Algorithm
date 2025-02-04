u=list(map(int,input().split()))
s=list(map(int,input().split()))

flag=0
us=0
ss=0
for i in range(8):
    us+=u[i]
    if us>ss:
        flag=1
    ss+=s[i]
    if us>ss:
        flag=1
us+=u[8]
if us > ss:
    flag = 1
ss+=s[8]
if flag and us<ss:
    print('Yes')
else:
    print('No')

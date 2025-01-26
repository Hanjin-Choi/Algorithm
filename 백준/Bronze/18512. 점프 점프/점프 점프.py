x,y,one,two = map(int,input().split())
s=set()
t=abs(one-two)
s.add(one)
flag=0
for i in range(t+y+1):
    one+=x
    s.add(one)
for j in range(t+x+2):
    if two in s:
        flag=1
        break
    else:
        two +=y

if flag:
    print(two)
else:
    print(-1)
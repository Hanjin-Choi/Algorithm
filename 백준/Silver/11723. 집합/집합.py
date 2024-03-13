import sys
input=sys.stdin.readline

m=int(input())
s=set()
for _ in range(m):
    inpt=input().strip()
    if inpt == 'all':
        s = {i for i in range(1,21)}
    elif inpt == 'empty':
        s = set()
    else:
        ipt,num=inpt.split()
        num=int(num)
        if ipt=='add':
            s.add(num)
        elif ipt=='check':
            if num in s:
                print(1)
            else:
                print(0)
        elif ipt=='remove' and num in s:
            s.remove(num)
        elif ipt=='toggle':
            if num in s:
                s.remove(num)
            else:
                s.add(num)



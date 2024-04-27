import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
s=input().strip()
t=0
p=2*n+1
idx=0
while idx <m-(2*n):
    if s[idx]=='O':
        idx+=1
    else:
        c=1
        for i in range(1,p):
            if i%2 and s[idx+i]=='I':
                idx += i
                break
            elif not i%2 and s[idx+i]=='O':
                idx += i
                break
            elif not i%2 and s[idx+i]=="I":
                c+=1
        if c ==n+1:
            t +=1
            idx+=2
print(t)
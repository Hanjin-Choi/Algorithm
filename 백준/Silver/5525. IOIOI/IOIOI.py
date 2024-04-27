import sys
input = sys.stdin.readline

n=int(input())
m=int(input())
s=input().strip()
t=0
p=1
idx=0
while idx <m-(2*n):
    if s[idx]=='O':
        idx+=1
    else:
        for i in range(p,2*n+1):
            if i%2 and s[idx+i]=='I':
                idx += i
                p = 1
                break
            elif not i%2 and s[idx+i]=='O':
                idx += i
                p = 1
                break
        else:
            t +=1
            idx+=2
            p=2*n-2

print(t)
import sys
input = sys.stdin.readline

def m(a,b,c):
    if b==1:
        return a%c
    if b %2:
        return (m(a,b//2,c)**2*a)%c
    else:
        return (m(a,b//2,c)**2)%c

a,b,c =map(int,input().split())
print(m(a,b,c))
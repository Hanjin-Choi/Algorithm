import sys
input = sys.stdin.readline

a,b = map(int,input().split())

def gcd(a,b):
    if b>a:
        b,a = a,b

    d, m = divmod(a,b)
    if m==0:
        return b
    else:
        return gcd(b,m)

GCD = gcd(a,b)
LCM = a*b//GCD
print(GCD)
print(LCM)
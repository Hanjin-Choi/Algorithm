def gcd(a,b):
    if a<b:
        a,b=b,a
    m,r = divmod(a,b)
    if r==0:
        return b
    else:
        return gcd(b,r)
n=int(input())
lst = list(map(int,input().split()))

mul = 1
s=0
for i in range(n):
    mul*=lst[i]
for i in range(n):
    s +=mul//lst[i]
m=gcd(s,mul)
print(mul//m,end='')
print('/',end='')
print(s//m,end='')

import sys
input = sys.stdin.readline

a,b =map(int,input().split())
last= int(b**0.5)+1
era = [0,0] + [1]*last
prime =[]
for e in range(2,last):
    if era[e]:
        prime.append(e)
        for i in range(e*2,last,e):
            era[i] =0
x=0
c=0
s=2
while x<len(prime):
    p=prime[x]
    if a<=p**s<=b:
        c += 1
        s += 1
    elif p**s<a:
        s +=1
    else:
        s=2
        x+=1
print(c)
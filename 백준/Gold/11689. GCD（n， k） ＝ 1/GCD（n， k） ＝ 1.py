import sys
input = sys.stdin.readline

n=int(input())
era =[0,0]+[1]*(int(n**0.5))
prime =n
p=[]
for i in range(2,int(n**0.5)+2):
    if era[i]:
        if n %i ==0:
            p.append(i)
            prime *= 1-1/i
        for j in range(i*2,int(n**0.5)+2,i):
            era[j] =0
x=0
while x < len(p):
    if n % p[x]==0:
        n//=p[x]
    else:
        x +=1
if n !=1:
    prime *= 1-1/n
print(int(prime))
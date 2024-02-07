import sys
import sys,math
input = sys.stdin.readline

n= int(input())
kl= list(map(int,input().split()))
al = [0]*len(kl)
era = [0,0]+[1]*(int(max(kl)**0.5))
prime=[]
for i in range(2,int(max(kl)**0.5)+1):
    if era[i]:
        prime.append(i)
        for j in range(i*2,int(max(kl)**0.5)+1,i):
            era[j]=0
if len(prime)==0:
    prime.append(2)
for i in range(n):
    all = []
    k=kl[i]
    x = 0
    while k>1:
        if x == len(prime):
            all.append(str(k))
            break
        elif k%prime[x] ==0:
            k //= prime[x]
            all.append(str(prime[x]))
        else:
            x +=1
    al[i] = " ".join(all)
print(*al,sep='\n')


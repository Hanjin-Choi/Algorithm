import sys
input = sys.stdin.readline
n=int(input())
# 소수 개수 구하기
era = [0] +[1]*(int((2*n-n//4-n//9+n//36)**0.5))
prime =[]
for i in range(2,int((2*n-n//4-n//9+n//36)**0.5)+1):
    if era[i]:
        prime.append(i)
        for j in range(i*2,int((2*n-n//4-n//9+n//36)**0.5)+1,i):
            era[j]=0
def func(num,mul,c,leng,s):
    ssum=0
    if s==leng or  mul >= num:
        return 0
    elif s<leng and c%2:
        for i in range(s,leng):
            ssum -= (num//(mul*prime[i]**2))
            if mul*prime[i]**2 <num:
                ssum += func(num,mul*(prime[i]**2),c+1,leng,i+1)
            else:
                break
    elif s < leng:
        for i in range(s,leng):
            ssum += num//(mul*prime[i]**2)
            if mul * prime[i] ** 2 < num:
                ssum += func(num, mul * (prime[i] ** 2), c + 1, leng, i + 1)
            else:
                break
    return ssum



leng = len(prime)
s = n+n//4+n//9 +n//25 - n//36 -n//225-n//100+n//900
e = 2*n-n//4-n//9+n//36
while s<=e:
    a=0
    m = (s+e)//2
    if m-func(m,1,0,leng,0) < n:
        s=m+1
    elif m-func(m,1,0,leng,0)>= n :
        e = m-1
print(s)
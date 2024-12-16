n=int(input())
cnt=0
m=1
while n>=10**m:
    cnt +=9*10**(m-1)*m
    cnt%=1234567
    m+=1
n-=(10**(m-1)-1)
cnt+=n*m
print(cnt%1234567)
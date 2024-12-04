n=int(input())
ans=1
while True:
    if n>10**ans:
        if n % 10**ans>=5*10**(ans-1):
            n=(n//10**ans+1)*10**ans
        else:
            n=(n//10**ans)*10**ans
        ans +=1
    else:
        print(n)
        break
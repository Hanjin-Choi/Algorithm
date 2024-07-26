sosu = [1]*10001
num=set()
for i in range(2,10001):
    if sosu[i]:
        num.add(i)
        for j in range(i*2,10001,i):
            sosu[j]=0

t=int(input())
for _ in range(t):
    n=int(input())
    x,y=n//2,n//2
    while True:
        if x in num and y in num:
            print(x,y)
            break
        else:
            x-=1
            y+=1
    
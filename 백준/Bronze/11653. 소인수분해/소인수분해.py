N=int(input())
n=1
while N !=1:
    odd = 2*n+1
    if N%2 ==0:
        print(2)
        N=N//2
    else:
        if N % odd==0:
            print(odd)
            N=N//odd
        else:
            n+=1

    
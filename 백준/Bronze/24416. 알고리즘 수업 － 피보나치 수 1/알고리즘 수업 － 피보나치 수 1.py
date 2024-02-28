n= int(input())
fib = [[0,0] for _ in range(n+1)]
fib[0]=[0,0]
fib[1]=[1,0]
fib[2]=[1,0]
for i in range(3,n+1):
    fib[i][0] += fib[i-1][0]+fib[i-2][0]
    fib[i][1] =i-2
print(*fib[n])
    
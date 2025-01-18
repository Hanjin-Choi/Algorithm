t =int(input())

for _ in range(t):
    a,b,c= map(int,input().split())
    print('Data set:',a,b,c)
    if a<b:
        a,b=b,a
    for time in range(c):
        a//=2
        if a<b:
            a,b=b,a
    print(a,b)
    print()
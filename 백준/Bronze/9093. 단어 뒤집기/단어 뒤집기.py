n= int(input())
for i in range(1,n+1):
    L = list(input()[::-1].split()[::-1])
    print(' '.join(L))
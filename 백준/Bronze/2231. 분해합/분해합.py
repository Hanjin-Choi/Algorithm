n = int(input())
L=[]
for _ in range(1,n):
    l=list(map(int,list(str(_))))

    L.append(_+sum(l))


    
if n in L:
    print(L.index(n)+1)
elif n not in L:
    print(0)
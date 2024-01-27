n = int(input())
L = []
for i in range(1,n+1):
    
    if i ==1:
        L.append(0)
    elif i ==2:
        L.append(1)
    elif i ==3:
        L.append(1)
    else:
        if i % 6 ==0:
            L.append(min(L[(i//3)-1],L[(i//2)-1],L[i-2])+1)
        elif i %3 ==0:
            L.append(min(L[(i//3)-1],L[i-2])+1)
        elif i %2 ==0:
            L.append(min(L[(i//2)-1],L[i-2])+1)
        else:
            L.append(L[i-2]+1)
print(L[n-1])

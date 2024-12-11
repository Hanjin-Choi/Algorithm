n=int(input())
m= int(n**0.5)+1
lst=[i for i in range(n+1)]
for i in range(n+1):
    for j in range(1,m):
        if i + j**2 <=n and lst[i+j**2]>lst[i]+1:
            lst[i+j**2]=lst[i]+1

print(lst[n])
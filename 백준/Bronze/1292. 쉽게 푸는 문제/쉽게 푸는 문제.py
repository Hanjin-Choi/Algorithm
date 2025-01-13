a,b = map(int,input().split())
lst =[0]
for i in range(1,46):
    lst += [i] * i

print(sum(lst[a:b+1]))
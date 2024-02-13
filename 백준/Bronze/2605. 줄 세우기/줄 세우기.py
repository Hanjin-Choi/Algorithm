n=int(input())
l=[i for i in range(1,n+1)]
sl=list(map(int,input().split()))
for i in range(n):
    num = l.pop(i)
    l.insert(i-sl[i],num)
print(*l)
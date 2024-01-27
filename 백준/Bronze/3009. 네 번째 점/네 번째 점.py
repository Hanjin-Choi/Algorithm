a,b = map(int,input().split())
c,d = map(int,input().split())
e,f = map(int,input().split())
x = [a,c,e]
y = [b,d,f]
for i in x:
    if x.count(i)==1:
        q=i
for j in y:
    if y.count(j)==1:
        w=j
print(q,w)
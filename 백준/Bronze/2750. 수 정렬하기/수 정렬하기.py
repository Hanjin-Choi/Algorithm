n= int(input())
s= set()
for _ in range(n):
    s.add(int(input()))
a=list(s)
a.sort()
for i in a:
    print(i)

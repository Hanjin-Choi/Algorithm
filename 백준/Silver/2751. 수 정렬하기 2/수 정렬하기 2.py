import sys
n= int(sys.stdin.readline())
l=[0]*n
for _ in range(n):
    a= int(sys.stdin.readline())
    l[_]=a
l.sort()
for i in l:
    print(i)

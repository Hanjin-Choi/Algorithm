import sys
input = sys.stdin.readline

n=int(input())
e= {}
l = {}
for i in range(n):
    name,status = input().split()
    e.setdefault(name,0)
    l.setdefault(name,0)
    if status=='enter':
        e[name] +=1
    else:
        l[name] +=1
l_name = []
for n in e:
    if e[n]-l[n]>0:
        l_name.append(n)
l_name.sort(reverse=True)
ans = '\n'.join(l_name)
print(ans)
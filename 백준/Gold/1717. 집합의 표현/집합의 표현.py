import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def find(x):
    if lst[x]==x:
        return x
    else:
        lst[x]=find(lst[x])
        return lst[x]

n,m = map(int,input().split())
lst=[i for i in range(n+1)]
for _ in range(m):
    num,a,b=map(int,input().split())
    if num==0:
        f= find(a)
        s=find(b)
        if f<=s:
            lst[s]=f
        else:
            lst[f]=s
    elif num==1:
        find(a)
        find(b)
        if lst[a]==lst[b]:
            print('yes')
        else:
            print('no')
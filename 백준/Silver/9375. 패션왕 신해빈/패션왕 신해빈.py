import sys
input = sys.stdin.readline

t=int(input())
for _ in range(t):
    dic={}
    n=int(input())
    for _ in range(n):
        clothes, kind = input().strip().split()
        if kind in dic:
            dic[kind].append(clothes)
        else:
            dic[kind]=[clothes]
    t=1
    for key in dic:
        t*=(len(dic[key])+1)
    print(t-1)
from collections import defaultdict
n=int(input())
d =defaultdict(int)
for _ in range(n):
    d[input()] += 1
ans=''
res=0
for key in d:
    if d[key]>res:
        ans=key
        res=d[key]
    elif d[key]==res and key<ans:
        ans=key

print(ans)

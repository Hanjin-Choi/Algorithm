import sys
input = sys.stdin.readline
u,n=map(int,input().split())

d = {i:[] for i in range(1,u+1)}
cnt = {i:0 for i in range(1,u+1)}
for _ in range(n):
    name, price = input().split()
    price = int(price)
    d[price].append(name)
    cnt[price]+=1
mini=n
for i in range(1,u+1):
    if cnt[i] and mini>cnt[i]:
        mini = cnt[i]
for i in range(1,u+1):
    if cnt[i]==mini:
        print(d[i][0],i)
        break

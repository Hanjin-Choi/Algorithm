import sys
input = sys.stdin.readline

n,k = map(int,input().split())
lst=set(int(input()) for _ in range(n))
res=[float('inf')]*10001
res[0]=0
for i in range(k):
    for j in lst:
        if i + j<=10000:
            res[i+j]=min(res[i+j],res[i]+1)
if res[k]==float('inf'):
    print(-1)
else:
    print(res[k])
import sys
input = sys.stdin.readline

n=int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
res = [0]*(n+1)
for i in range(1,n+1):
    if i+lst[i-1][0]-1<=n:
        res[i+lst[i-1][0]-1] = max(res[i-1]+lst[i-1][1],res[i+lst[i-1][0]-1])
        res[i]=max(res[i],res[i-1])
    else:
        res[i]=max(res[i],res[i-1])
print(res[n])
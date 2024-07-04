import sys
input = sys.stdin.readline

n = int(input())
lst=list(map(int,input().split()))
res=[1]*n
for i in range(1,n):
    for j in range(i):
        if lst[i]>lst[j]:
            res[i]=max(res[i],res[j]+1)
print(max(res))
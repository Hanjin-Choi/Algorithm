import sys
input = sys.stdin.readline

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]

ans=1000*n
for first in range(3):
    remember=[1000*n]*3
    remember[first]=arr[0][first]
    for row in range(1,n):
        res=[0]*3
        res[0] = arr[row][0] + min(remember[1],remember[2])
        res[1] = arr[row][1] + min(remember[0], remember[2])
        res[2] = arr[row][2] + min(remember[1], remember[0])
        remember=res
    for idx in range(3):
        if first ==idx: continue
        ans=min(ans,remember[idx])
print(ans)
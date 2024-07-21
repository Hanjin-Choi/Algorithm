import sys
input = sys.stdin.readline
dm=[(0,1),(1,0),(1,1)]

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
ans=[[[0,0,0]for _ in range(n)] for _ in range(n)]
ans[0][1][0]=1
for row in range(n):
    for col in range(n):
        if (row,col) ==(0,0) or(row,col) ==(0,1):
            continue
        elif arr[row][col]:
            continue
        else:
            if 0<=col-1<n:
                ans[row][col][0] += ans[row][col-1][0]+ ans[row][col-1][2]
            if 0<=row-1<n:
                ans[row][col][1] += ans[row-1][col][1]+ ans[row-1][col][2]
            if 0<=col-1<n and 0<=row-1<n and not arr[row-1][col] and not arr[row][col-1] and not arr[row-1][col-1]:
                ans[row][col][2]+=sum(ans[row-1][col-1])
print(sum(ans[n-1][n-1]))
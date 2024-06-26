import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
for row in range(n):
    for col in range(n):
        if col!=0:
            arr[row][col] += arr[row][col-1]
        if row!=0:
            arr[row][col] += arr[row-1][col]
        if row>0 and col>0:
            arr[row][col] -=arr[row-1][col-1]
            
for _ in range(m):
    x1,y1,x2,y2=map(int,input().split())
    ans = arr[x2-1][y2-1]
    if x1>1 and y1>1:
        ans+=arr[x1-2][y1-2]-arr[x2-1][y1-2]-arr[x1-2][y2-1]
    elif x1>1:
        ans-=arr[x1-2][y2-1]
    elif y1>1:
        ans-=arr[x2-1][y1-2]
    print(ans)
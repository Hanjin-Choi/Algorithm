import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dr=[1,-1,0,0]
dc=[0,0,-1,1]
def dfs(r,c):
    arr[r][c]=0
    for i in range(4):
        row = r + dr[i]
        col = c + dc[i]
        if 0<=row<n and 0<=col<m and arr[row][col]:
            arr[row][col]=0
            dfs(row,col)
    return

t=int(input())
for tc in range(t):
    m,n,k=map(int,input().strip().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        c,r = map(int,input().strip().split())
        arr[r][c]=1
    count_worm =0
    for row in range(n):
        for col in range(m):
            if arr[row][col]:
                dfs(row,col)
                count_worm+=1

    print(count_worm)
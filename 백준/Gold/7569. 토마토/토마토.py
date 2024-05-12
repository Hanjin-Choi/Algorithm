import sys
input = sys.stdin.readline
from collections import deque
m,n,h = map(int,input().strip().split())
arr = [list(map(int,input().strip().split())) for _ in range(n*h)]
dr=[0,0,-1,1]
dc=[1,-1,0,0]

def findto():
    lst=[]
    for r in range(n*h):
        for c in range(m):
            if arr[r][c]==1:
                hei,row = divmod(r,n)
                lst.append((row,c,hei,0))
    return lst

def bfs(lst):
    if not lst:
        return -1
    q=deque(lst)
    while q:
        r,c,hi,cnt = q.popleft()
        for i in range(4):
            row = r+dr[i]
            col = c+dc[i]
            if n*hi<=row+hi*n<n*hi+n and 0<=col<m and not arr[row+hi*n][col]:
                arr[row + hi * n][col]=1
                q.append((row,col,hi,cnt+1))
        if 0<=r+hi*n+n<n*h and not arr[r+hi*n+n][c]:
            arr[r+hi*n+n][c]=1
            q.append((r,c,hi+1,cnt+1))
        if 0<=r+hi*n-n<n*h and not arr[r+hi*n-n][c]:
            arr[r+hi*n-n][c]=1
            q.append((r,c,hi-1,cnt+1))
    return cnt
def check():
    for r in range(n*h):
        for c in range(m):
            if not arr[r][c]:
                return -1

    return 0

li = findto()
cnt=bfs(li)
res=check()
if res:
    print(res)
else:
    print(cnt)
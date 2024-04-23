import sys
input=sys.stdin.readline
from collections import deque
dr=[0,1,-1,0]
dc=[1,0,0,-1]
def bfs():
    q=deque()
    q.append((0,0,1))
    while q:
        row,col,t = q.popleft()
        if row ==n-1 and col ==m-1:
            return t
        for i in range(4):
            r=row + dr[i]
            c=col+dc[i]
            if 0<=r<n and 0<=c<m and arr[r][c]:
                arr[r][c]=0
                q.append((r,c,t+1))
n,m = map(int,input().split())
arr = [list(map(int,list(input().strip()))) for _ in range(n)]
arr[0][0]=0
print(bfs())

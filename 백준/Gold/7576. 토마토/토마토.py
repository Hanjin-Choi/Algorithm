import sys
input = sys.stdin.readline
from collections import deque
def findtoma():
    lst=[]
    cnt =0
    for row in range(n):
        for col in range(m):
            if arr[row][col]==1:
                cnt+=1
                lst.append((row,col))
    return lst,cnt
dr=[0,0,1,-1]
dc=[1,-1,0,0]
def bfs():
    while q:
        r,c,cnt = q.popleft()
        for idx in range(4):
            rr=r+dr[idx]
            cc=c+dc[idx]
            if 0<=rr<n and 0<=cc<m and arr[rr][cc]==0:
                arr[rr][cc]=cnt+1
                q.append((rr,cc,cnt+1))
def maxx():
    max = 0
    for row in range(n):
        for col in range(m):
            if (row,col) in lst: continue
            if max < arr[row][col]:
                max = arr[row][col]
            if arr[row][col] == 0:
                return -1
    return max
m,n = map(int,input().strip().split())
arr= [list(map(int,input().strip().split())) for _ in range(n)]
lst,cnt = findtoma()
if cnt == m*n:
    print(0)
else:
    q=deque()
    for r,c in lst:
        q.append((r,c,0))
    bfs()
    lst=set(lst)
    ans=maxx()
    print(ans)
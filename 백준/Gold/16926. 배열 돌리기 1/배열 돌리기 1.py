import sys
input = sys.stdin.readline
from collections import deque
dr=[0,1,0,-1]
dc=[1,0,-1,0]
def turn(row):
    q=deque()
    r=c=row
    i=0
    while i<4:
        if not visit[r][c]:
            q.append(arr[r][c])
            visit[r][c]=1
        if 0<=r+dr[i]<n and 0<=c+dc[i]<m and not visit[r+dr[i]][c+dc[i]]:
            r+=dr[i]
            c+=dc[i]
        elif i<3:
            i+=1
            r += dr[i]
            c += dc[i]
        else:
            i+=1
    q.rotate(-t)
    i=0
    rr=cc=row
    while i<4:
        if not visit2[rr][cc]:
            arr[rr][cc] = q.popleft()
            visit2[rr][cc]=1
        if 0 <= rr+dr[i] < n and 0 <= cc+dc[i] < m and not visit2[rr+dr[i]][cc+dc[i]]:
            rr += dr[i]
            cc += dc[i]
        elif i<3:
            i += 1
            rr += dr[i]
            cc += dc[i]
        else:
            i += 1


n,m,t = map(int,input().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
visit =[[0]*m for _ in range(n)]
visit2 =[[0]*m for _ in range(n)]

for row in range(n):
    if not visit[row][row]:
        turn(row)
    else:
        break
for row in range(n):
    print(*arr[row])
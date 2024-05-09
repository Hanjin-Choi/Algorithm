import sys
input = sys.stdin.readline
from collections import deque
dr =[1,-1,0,0]
dc= [0,0,1,-1]

def find():

    for row in range(n):
        for col in range(m):
            if arr[row][col]=='I':
                return (row,col)

def bfs(r,c):
    num=0
    q=deque()
    q.append((r,c))
    while q:
        row,col=q.popleft()
        visit[row][col]=1
        if arr[row][col]=='P':
            num+=1
        for i in range(4):
            rr=row + dr[i]
            cc=col + dc[i]
            if 0<=rr<n and 0<=cc<m and arr[rr][cc] !='X' and not visit[rr][cc]:
                q.append((rr,cc))
                visit[rr][cc]=1
    return num


n,m= map(int,input().split())
arr=[list(input().strip()) for _ in range(n)]
visit =[[0]*m for _ in range(n)]
r,c=find()
res= bfs(r,c)
if res:
    print(res)
else:
    print('TT')
import sys
input = sys.stdin.readline
from collections import deque

dm=[(1,0),(0,1),(-1,0),(0,-1)]

def move(ro,co):
    people=arr[ro][co]
    cnt=1
    q=deque([(ro,co)])
    q2=[(ro,co)]
    visit[ro][co]=1
    while q:
        rr,cc=q.popleft()
        for i in range(4):
            rrr=rr+dm[i][0]
            ccc = cc + dm[i][1]
            if 0<=rrr<n and 0<=ccc<n and not visit[rrr][ccc] and l<=abs(arr[rr][cc]-arr[rrr][ccc])<=r:
                visit[rrr][ccc]=1
                people +=arr[rrr][ccc]
                q.append((rrr,ccc))
                q2.append((rrr,ccc))
                cnt+=1
    if cnt ==1:
        return 0
    else:
        temp = people//cnt
        for idx in range(cnt):
            arr[q2[idx][0]][q2[idx][1]]=temp
        return 1


n,l,r=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(n)]
day=0
while True:
    visit=[[0]*n for _ in range(n)]
    total=0
    for row in range(n):
        for col in range(n):
            if not visit[row][col]:
                total+=move(row,col)
    if not total:
        break
    day+=1
print(day)
import sys
input = sys.stdin.readline
from collections import deque
dr=[1,-1,0,0]
dc=[0,0,-1,1]
def sheepwolf(row,col):
    sheep = 0
    wolf = 0
    if arr[row][col] =='v':
        wolf+=1
    elif arr[row][col]=='o':
        sheep +=1
    q=deque([(row,col)])
    while q:
        ro, co = q.popleft()
        for i in range(4):
            rr=ro+dr[i]
            cc=co+dc[i]
            if 0<=rr<r and 0<=cc<c and not visit[rr][cc]:
                visit[rr][cc] = 1
                if arr[rr][cc]=='#':
                    continue
                elif arr[rr][cc]=='v':
                    wolf +=1
                elif arr[rr][cc]=='o':
                    sheep +=1
                q.append((rr, cc))
    if sheep>wolf:
        return sheep,0
    else:
        return 0,wolf

r,c =map(int,input().split())
arr= [list(input().strip()) for _ in range(r)]
visit = [[0]*c for _ in range(r)]
s=w=0
for row in range(r):
    for col in range(c):
        if not visit[row][col] and arr[row][col] =='#':
            visit[row][col]=1
        elif not visit[row][col]:
            visit[row][col]=1
            sh,wf =sheepwolf(row,col)
            s+=sh
            w+=wf
print(s,w)
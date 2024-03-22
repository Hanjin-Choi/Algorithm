from collections import deque
t=int(input())
dr=[1,0,0,-1]
dc=[0,1,-1,0]
def bfs():
    q=deque([(0,0)])
    visit=[[float('inf')]*n for _ in range(n)]
    visit[0][0]=0
    while q:
        r,c= q.popleft()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<n and 0<=cc<n:
                s =visit[r][c]+int(arr[rr][cc])
                if visit[rr][cc]>s:
                    visit[rr][cc]=s
                    q.append((rr,cc))
    return visit[n-1][n-1]

for tc in range(1,t+1):
    n=int(input())
    arr=[list(input()) for _ in range(n)]
    res=bfs()
    print(f'#{tc} {res}')
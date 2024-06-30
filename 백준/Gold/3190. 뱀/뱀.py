import sys
input = sys.stdin.readline
from collections import deque
dm=[(0,1),(1,0),(0,-1),(-1,0)]
def move(t,i):
    flag=0
    for time in range(1,t+1):
        row,col=snake[0]
        rr=row + dm[i][0]
        cc=col + dm[i][1]
        if 1<=rr<=n and 1<=cc<=n and arr[rr][cc]<=1:
            if arr[rr][cc]==1:
                snake.appendleft((rr,cc))
                arr[rr][cc]=2
            elif arr[rr][cc]==0:
                tail_row,tail_col = snake.pop()
                arr[tail_row][tail_col]=0
                snake.appendleft((rr,cc))
                arr[rr][cc]=2
        else:
            flag=1
            break
    return time,flag
n=int(input())
k=int(input())
arr = [[0]*(n+1) for _ in range(n+1)]
for _ in range(k):
    r,c =map(int,input().split())
    arr[r][c]=1
l=int(input())
idx=0

snake =deque([(1,1)])
arr[1][1]=2
ans=0
for _ in range(l):
    x,c = input().split()
    cnt, flag=move(int(x)-ans,idx)
    ans+=cnt
    if flag:
        break
    if c =='D':
        idx+=1
        idx%=4
    else:
        idx-=1
        idx%=4
else:
    cnt, flag = move(n, idx)
    ans += cnt
print(ans)
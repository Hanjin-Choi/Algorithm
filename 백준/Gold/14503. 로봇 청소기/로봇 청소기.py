import sys
input = sys.stdin.readline
dr=[-1,0,1,0]
dc=[0,1,0,-1]
def move(i,j,k):
    global cnt
    if arr[i][j]==0:
        arr[i][j]=2
        cnt+=1
    elif arr[i][j]==1:
        return
    for idx in range(1,5):
        di = (k - idx)%4
        r=i+dr[di]
        c=j+dc[di]
        if arr[r][c]==0:
            move(r,c,di)
            break
    else:
        di = (k+2)%4
        r=i+dr[di]
        c=j + dc[di]
        move(r,c,k)

n,m = map(int,input().split())
i,j,k =map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(n)]
cnt=0
move(i,j,k)
print(cnt)
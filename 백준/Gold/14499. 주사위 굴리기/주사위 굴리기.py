import sys
input = sys.stdin.readline

def roll(idx):
    u,d,f,b,l,r=dice
    global x,y
    xx=x+dm[idx][0]
    yy=y+dm[idx][1]
    if 0<=xx<n and 0<=yy<m:
        if idx==1:
            dice[0],dice[1],dice[4],dice[5]=l,r,d,u
        elif idx==2:
            dice[0], dice[1], dice[4], dice[5] = r, l, u, d
        elif idx==3:
            dice[0], dice[1], dice[2], dice[3] = f, b, d, u
        elif idx==4:
            dice[0], dice[1], dice[2], dice[3] = b, f, u, d
        x,y=xx,yy
        if arr[x][y]:
            dice[1],arr[x][y]=arr[x][y],0
        else:
            arr[x][y]=dice[1]
        print(dice[0])


dm=[(0,0),(0,1),(0,-1),(-1,0),(1,0)]
n,m,x,y,k=map(int,input().split())
dice=[0]*6 #u,d,f,b,l,r
arr= [list(map(int,input().split())) for _ in range(n)]
command=list(map(int,input().split()))
for i in command:
    roll(i)
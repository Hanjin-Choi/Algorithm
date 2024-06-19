import sys
input = sys.stdin.readline
dm=[(0,1),(-1,0),(0,-1),(1,0)]
def condition():
    condi=[]
    for row in range(r):
        if arr[row][0]==-1:
            condi.append(row)
    return condi
def dust():
    temp=[[0]*c for _ in range(r)]
    for row in range(r):
        for col in range(c):
            temp[row][col]+=arr[row][col]
            if arr[row][col]>0:
                for i in range(4):
                    rr=row+dm[i][0]
                    cc = col + dm[i][1]
                    if 0<=rr<r and 0<=cc<c and (rr,cc)!=(con[0],0) and (rr,cc)!=(con[1],0):
                        temp[rr][cc]+=arr[row][col]//5
                        temp[row][col]-=arr[row][col]//5
    return temp
def move():
    for i in range(2):
        row = con[i]
        col=1
        idx=0
        temp = arr[row][col]
        arr[row][col]=0
        while True:
            if 0<=row+dm[idx][0]<r and 0<=col+dm[idx][1]<c:
                row += dm[idx][0]
                col += dm[idx][1]
                if (row,col)==(con[i],0):
                    break
                arr[row][col],temp=temp,arr[row][col]
            elif i==0:
                idx+=1
            elif i==1:
                idx-=1




r,c,t=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(r)]
con = condition()
for _ in range(t):
    arr=dust()
    move()
total_dust=2
for row in range(r):
    for col in range(c):
        total_dust +=arr[row][col]
print(total_dust)
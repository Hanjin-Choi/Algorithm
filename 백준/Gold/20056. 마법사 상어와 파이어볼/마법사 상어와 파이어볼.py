import sys
input = sys.stdin.readline

def move():
    temp=[]
    coord=set()
    for row,col in ball:
        for m,s,d in arr[row][col]:
            nr=row + dr[d][0]*s
            nr %=n
            nc=col + dr[d][1]*s
            nc %=n
            temp.append((nr,nc,m,s,d))
            coord.add((nr,nc))
        arr[row][col]=[]
    for r,c,m,s,d in temp:
        arr[r][c].append((m,s,d))
    return list(coord)
def endmove():
    for row,col in ball:
        flag=arr[row][col][0][2]%2
        total_m = 0
        total_s=0
        leng=len(arr[row][col])
        if leng>1:
            for m,s,d in arr[row][col]:
                total_m+=m
                total_s+=s
                if d%2 != flag:
                    flag=2
            total_m//=5
            total_s//=leng
            arr[row][col]=[]
            if total_m>0 and flag!=2:
                for dir in (0,2,4,6):
                    arr[row][col].append((total_m,total_s,dir))
            elif total_m>0 and flag==2:
                for dir in (1,3,5,7):
                    arr[row][col].append((total_m,total_s,dir))


dr=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]
n,m,k =map(int,input().split())
arr =[[[] for _ in range(n)] for _ in range(n)]
ball=[]
weight=0
for _ in range(m):
    r,c,m,s,d =map(int,input().split())
    arr[r-1][c-1].append((m,s,d))
    ball.append((r-1,c-1))
for _ in range(k):
    ball=move()
    endmove()
for row,col in ball:
    for m,s,d in arr[row][col]:
        weight+=m
print(weight)
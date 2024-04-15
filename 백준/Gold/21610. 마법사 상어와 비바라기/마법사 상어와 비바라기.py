import sys
input = sys.stdin.readline
from collections import deque
dr =[0,0,-1,-1,-1,0,1,1,1]
dc =[0,-1,-1,0,1,1,1,0,-1]
ddr=[1,1,-1,-1]
ddc=[1,-1,-1,1]
def move_cloud(d,s):
    while cloud:
        r,c = cloud.pop()
        r += dr[d]*s
        c += dc[d]*s
        r%=n
        c%=n
        arr[r][c]+=1
        temp_cloud.add((r,c))

def make_cloud():
    for row in range(n):
        for col in range(n):
            if arr[row][col]>=2 and not (row,col) in temp_cloud:
                arr[row][col]-=2
                cloud.append((row,col))

n,m = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]
cloud =[(n-1,0),(n-1,1),(n-2,0),(n-2,1)]
for _ in range(m):
    temp_cloud = set()
    d,s= map(int,input().split())
    move_cloud(d,s)
    for r,c in temp_cloud:
        for i in range(4):
            rr= r+ddr[i]
            cc= c+ddc[i]
            if 0<=rr<n and 0<=cc<n and arr[rr][cc]:
                arr[r][c]+=1
    make_cloud()
total=0
for row in range(n):
    total +=sum(arr[row])
print(total)


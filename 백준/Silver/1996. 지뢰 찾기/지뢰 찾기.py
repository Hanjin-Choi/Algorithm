import sys
input = sys.stdin.readline

dr=[1,1,1,0,0,-1,-1,-1]
dc=[-1,0,1,-1,1,-1,0,1]
def mine(r,c):
    m =0
    if arr[r][c].isnumeric():
        return '*'
    for i in range(8):
        rr=r+dr[i]
        cc=c+dc[i]
        if 0<=rr<n and 0<=cc<n and arr[rr][cc].isnumeric():
            m+=int(arr[rr][cc])
    if m>=10:
        return 'M'
    return str(m)
n=int(input())
arr = [list(input()) for _ in range(n)]
ans = [[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        ans[row][col]=mine(row,col)

for r in range(n):
    print(''.join(ans[r]))
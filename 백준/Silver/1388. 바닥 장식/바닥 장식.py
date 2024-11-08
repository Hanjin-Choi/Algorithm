import sys
input = sys.stdin.readline
row,col = map(int,input().split())
arr = [input().strip() for _ in range(row)]

cnt=0
visit = [[0]*col for _ in range(row)]

for r in range(row):
    for c in range(col):
        if not visit[r][c]:
            cnt+=1
            rr=r
            cc=c
            if arr[r][c] =='-':
                while 0<=cc<col and arr[rr][cc]=='-':
                    visit[rr][cc] = 1
                    cc+=1
            else:
                while  0<=rr<row and arr[rr][cc]== '|':
                    visit[rr][cc]=1
                    rr+=1
print(cnt)
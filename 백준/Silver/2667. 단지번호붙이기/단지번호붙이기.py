import sys
input = sys.stdin.readline
dr=[1,-1,0,0]
dc=[0,0,1,-1]
def bfs(r,c):
    visit[r][c]=1
    st=[(r,c)]
    cnt=1
    while st:
        r,c=st.pop()
        for i in range(4):
            rr=r+dr[i]
            cc=c+dc[i]
            if 0<=rr<n and 0<=cc<n and not visit[rr][cc]:
                st.append((rr,cc))
                visit[rr][cc]=1
                cnt+=1
    return cnt


n=int(input())
arr=[list(input()) for _ in range(n)]
visit=[[0 if arr[j][i]=='1' else 1 for i in range(n)] for j in range(n)]
ans=[]
for row in range(n):
    for col in range(n):
        if not visit[row][col]:
            ans.append(bfs(row,col))
ans.sort()
print(len(ans))
print(*ans,sep='\n')
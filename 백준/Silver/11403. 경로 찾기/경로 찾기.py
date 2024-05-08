import sys
input = sys.stdin.readline

def dfs(i):
    st=[]
    st.append(i)
    while st:
        pre = st.pop()
        for j in range(n):
            if arr[pre][j] and not visit[pre][j]:
                ans[i][j]=1
                visit[pre][j]=1
                st.append(j)
n=int(input())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
ans=[[0]*n for _ in range(n)]
for start in range(n):
    visit=[[0]*n for _ in range(n)]
    dfs(start)
for row in range(n):
    print(*ans[row])
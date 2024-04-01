import sys
input = sys.stdin.readline
from collections import deque
def bfs(x):
    visit[x]=0
    q=deque([x])
    while q:
        present = q.popleft()
        if visit[present]==k:continue
        for w in adjl[present]:
            if visit[w]>visit[present]+1:
                visit[w]=visit[present]+1
                q.append(w)
n,m,k,x = map(int,input().split())
adjl = [[] for _ in range(n+1)]
visit =[float('inf')]*(n+1)
for _ in range(m):
    a,b =map(int,input().split())
    adjl[a].append(b)
bfs(x)
cnt=0
ans=[]
for idx in range(1,n+1):
    if visit[idx]==k:
        cnt+=1
        ans.append(idx)
if cnt==0:
    print(-1)
else:
    print(*ans,sep='\n')
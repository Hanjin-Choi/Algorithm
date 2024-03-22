t=int(input())
def dfs(i):
    visit[i]=1
    for w in adjl[i]:
        if not visit[w]:
            dfs(w)

for tc in range(1,t+1):
    n,m = map(int,input().split())
    visit=[0]*(n+1)
    adjl =[[]for _ in range(n+1)]
    for _ in range(m):
        s,e = map(int,input().split())
        adjl[s].append(e)
        adjl[e].append(s)
    cnt=0
    for i in range(1,n+1):
        if not visit[i]:
            dfs(i)
            cnt+=1
    print(f'#{tc} {cnt}')
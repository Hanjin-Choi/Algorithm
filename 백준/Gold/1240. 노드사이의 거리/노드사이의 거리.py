import sys
input = sys.stdin.readline

def dfs(s,e,l):
    if s==e:
        return l
    else:
        for p, dist in adjl[s]:
            if not visit[p]:
                visit[p]=1
                res=dfs(p,e,l+dist)
                if res:
                    return res
                visit[p]=0
    return

n,m =map(int,input().split())
adjl=[[] for _ in range(n+1)]

for _ in range(n-1):
    s,e,d = map(int,input().split())
    adjl[s].append((e,d))
    adjl[e].append((s,d))
for _ in range(m):
    visit = [0] * (n + 1)
    start,end = map(int,input().split())
    visit[start]=1
    print(dfs(start,end,0))

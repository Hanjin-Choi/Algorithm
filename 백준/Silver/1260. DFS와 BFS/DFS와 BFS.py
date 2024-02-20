import sys
input = sys.stdin.readline

def dfs(s):
    visited_dfs[s]=1
    print(s, end=" ")
    for w in adjl[s]:
        if not visited_dfs[w]:
            dfs(w)

def bfs(s):
    q.append(s)
    while q:
        a= q.pop(0)
        if not visited_bfs[a]:
            visited_bfs[a] = 1
            print(a,end=' ')
            for w in adjl[a]:
                if not visited_bfs[w]:
                    q.append(w)


v,e,s = map(int,input().split())
adjl = [[] for _ in range(v+1)]
visited_dfs = [0]*(v+1)
visited_bfs = [0]*(v+1)
q=[]
for i in range(e):
    n1, n2 = map(int,input().split())
    adjl[n1].append(n2)
    adjl[n2].append(n1)
for i in range(v+1):
    adjl[i].sort()
dfs(s)
print()
bfs(s)
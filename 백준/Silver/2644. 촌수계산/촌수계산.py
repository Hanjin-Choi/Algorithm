from collections import deque
n=int(input())
s,e = map(int,input().split())
m=int(input())
adjl = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    adjl[x].append(y)
    adjl[y].append(x)
cnt = -1
q=deque()
q.append((0,s))
visit = [0]*(n+1)
visit[s]=1
while q:
    c, now = q.popleft()
    if now == e:
        cnt = c
        break
    for w in adjl[now]:
        if not visit[w]:
            q.append((c+1,w))
            visit[w]=1
print(cnt)
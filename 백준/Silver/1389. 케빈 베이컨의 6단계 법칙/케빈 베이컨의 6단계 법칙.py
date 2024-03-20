import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    visit = [0]*(n+1)
    queue=deque()
    queue.append(s)
    while queue:
        a=queue.popleft()
        for w in friends[a]:
            if not visit[w]:
                visit[w]=visit[a]+1
                queue.append(w)
    return sum(visit)
n,m = map(int,input().strip().split())
friends =[[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().strip().split())
    friends[a].append(b)
    friends[b].append(a)
minn=float('inf')
user=[]
for i in range(1,n+1):
    res=bfs(i)
    if res<minn:
        user=[i]
        minn=res
    elif res==minn:
        user.append(i)
user.sort()
print(user[0])

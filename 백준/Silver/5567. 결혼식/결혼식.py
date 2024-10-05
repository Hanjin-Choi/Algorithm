import sys
input = sys.stdin.readline
from collections import defaultdict,deque

def bfs():
    q=deque()
    visit[1]=1
    q.append((1,0))

    while q:
        now,cnt =q.popleft()
        if cnt ==2 : continue
        for friend in graph[now]:
            if visit[friend]:
                continue
            visit[friend]=1
            q.append((friend,cnt+1))
n = int(input())
m= int(input())
graph = defaultdict(set)
visit = [0]*(n+1)
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].add(b)
    graph[b].add(a)

bfs()
print(sum(visit)-1)
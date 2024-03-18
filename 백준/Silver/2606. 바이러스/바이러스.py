import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que=deque([1])
    visit[1]=1
    c=0
    while que:
        now = que.popleft()
        for i in adjl[now]:
            if not visit[i]:
                visit[i]=1
                que.append(i)
                c+=1
    return c
com=int(input())
couple=int(input())
adjl=[[] for _ in range(com+1)]
visit=[0]*(com+1)
for _ in range(couple):
    a,b = map(int,input().split())
    adjl[a].append(b)
    adjl[b].append(a)
print(bfs())
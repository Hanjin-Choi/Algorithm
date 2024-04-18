import sys
input = sys.stdin.readline
from collections import deque
def bfs():
    while q:
        x,y = q.popleft()
        if abs(x - festival[0]) + abs(y - festival[1])<=1000:
            return 1
        for i in range(n):
            if abs(x-store[i][0])+abs(y-store[i][1])<=1000 and not visit[i]:
                q.append((store[i][0],store[i][1]))
                visit[i]=1
    return 0

t=int(input())
for tc in range(t):
    n=int(input())
    home = list(map(int,input().split()))
    store =[list(map(int,input().split())) for _ in range(n)]
    festival = list(map(int,input().split()))
    q=deque()
    visit =[0]*n
    q.append((home[0],home[1]))
    flag =bfs()
    if flag:
        print('happy')
    else:
        print('sad')
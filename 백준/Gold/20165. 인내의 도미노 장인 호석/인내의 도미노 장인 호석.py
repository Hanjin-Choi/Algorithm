import sys
input = sys.stdin.readline
from collections import deque
def move():
    x,y,dir = input().split()
    x=int(x)-1
    y=int(y)-1
    q =deque([(x,y)])
    cnt =1
    if dir =="N":
        while q:
            a,b = q.popleft()
            ans[a][b]='F'
            t = arr[a][b]
            for idx in range(1,t):
                rr=a -idx
                if 0<=rr<n and ans[rr][b]=='S':
                    ans[rr][b]='F'
                    cnt+=1
                    q.append((rr,b))
    elif dir == "S":
        while q:
            a, b = q.popleft()
            ans[a][b] = 'F'
            t = arr[a][b]
            for idx in range(1, t):
                rr = a + idx
                if 0 <= rr < n and ans[rr][b] == 'S':
                    ans[rr][b] = 'F'
                    cnt += 1
                    q.append((rr, b))
    elif dir == "E":
        while q:
            a, b = q.popleft()
            ans[a][b] = 'F'
            t = arr[a][b]
            for idx in range(1, t):
                cc = b + idx
                if 0 <= cc < m and ans[a][cc]=='S':
                    ans[a][cc] = 'F'
                    cnt += 1
                    q.append((a, cc))

    elif dir == "W":
        while q:
            a, b = q.popleft()
            ans[a][b] = 'F'
            t = arr[a][b]
            for idx in range(1, t):
                cc = b - idx
                if 0 <= cc < m and ans[a][cc] == 'S':
                    ans[a][cc] = 'F'
                    cnt += 1
                    q.append((a, cc))
    return cnt
def stand():
    x,y = map(int,input().split())
    ans[x-1][y-1]='S'

n,m,r = map(int,input().split())
arr = [list(map(int,input().strip().split())) for _ in range(n)]
ans = [['S']*m for _ in range(n)]
total=0
for i in range(r):
    total +=move()
    stand()
print(total)
for i in range(n):
    print(*ans[i])
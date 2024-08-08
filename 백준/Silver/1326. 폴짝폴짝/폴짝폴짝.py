from collections import deque
n=int(input())
lst=list(map(int,input().split()))
a,b=map(int,input().split())
def find(a,b):
    q=deque()
    q.append((0,a-1))
    visit=[0]*n
    visit[a-1]=1
    cnt=-1
    while q:
        c,now = q.popleft()
        for i in range(-n,n):
            post =lst[now]*i+now
            if post == b-1:
                cnt=c+1
                return cnt
            elif 0<=post<n and not visit[post]:
                visit[post]=1
                q.append((c+1,post))
    return cnt
print(find(a,b))
import sys
input = sys.stdin.readline

n=int(input())
l=[0]+[int(input()) for _ in range(n)]
visit =[0]*(n+1)
visit[1]=l[1]
if n>1:
    visit[2]=l[2]+l[1]
for idx in range(3,n+1):
    visit[idx] = max(visit[idx-2],visit[idx-3]+l[idx-1])+l[idx]
print(visit[n])

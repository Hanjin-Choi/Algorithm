import sys
from collections import deque

input = sys.stdin.readline
q=deque()
n=int(input())
cnt=0
maxy=0
mini=1000001
for _ in range(n):
    s= input()
    if s[0]=='1':
        act,num=map(int,s.split())
        q.append(num)
        cnt+=1
    if s[0]=='2':
        q.popleft()
        cnt-=1
    if maxy<cnt:
        maxy=cnt
        mini=q[-1]
    elif maxy==cnt and mini >q[-1]:
        mini=q[-1]
print(maxy,mini)
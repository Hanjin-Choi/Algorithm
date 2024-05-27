import sys
input = sys.stdin.readline
from collections import deque

def findp():
    q = deque([1])
    while q:
        num = q.popleft()
        for i in adjl[num]:
            if not p[i]:
                p[i] = num
                q.append(i)

n=int(input())
p =[0]*(n+1)
p[1]=1
adjl = [[]for _ in range(n+1)]
for _ in range(n-1):
    first, second = map(int,input().split())
    adjl[first].append(second)
    adjl[second].append(first)
findp()
for idx in range(2,n+1):
    print(p[idx])
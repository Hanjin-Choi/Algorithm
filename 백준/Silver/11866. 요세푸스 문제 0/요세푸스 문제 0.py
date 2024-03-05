import sys
input = sys.stdin.readline
from collections import deque


n,k = map(int,input().split())
l= deque([i for i in range(1,n+1)])
ans ='<'
while l:
    l.rotate(-k+1)
    ans += str(l.popleft()) + ', '
ans=ans[:-2]+'>'
print(ans)
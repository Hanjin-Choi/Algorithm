import sys
input = sys.stdin.readline
from collections import deque
n,m = map(int,input().split())
lst= list(map(int,input().split()))


q=deque([i for i in range(1,n+1)])
cnt=0
for i in range(m):
    idx=0
    leng=len(q)
    for j in range(leng):
        if q[j]==lst[i]:
            if idx <= leng//2:
                q.rotate(-idx)
                q.popleft()
                cnt+=idx
            else:
                q.rotate(leng-idx)
                q.popleft()
                cnt += leng-idx
            break
        else:
            idx+=1

print(cnt)
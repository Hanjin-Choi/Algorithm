import sys
input = sys.stdin.readline
from collections import deque
n=int(input())
lst = list(map(int,input().split()))
idx1=0
idx2=1
cnt=1
temp=0
q=deque([lst[0]])
while idx2<n and idx1+cnt <n:
    if len(q)==1 and lst[idx1]==lst[idx2]:
        idx2+=1
    elif len(q)==1:
        q.append(lst[idx2])
        temp=idx2
        idx2+=1
    elif len(q)==2 and lst[idx2]==q[1]:
        idx2+=1
    elif len(q)==2 and lst[idx2]==q[0] and lst[temp]!=lst[idx2]:
        q.rotate(1)
        temp=idx2
        idx2+=1
    elif len(q)==2 and lst[idx2] not in q:
        q.popleft()
        if idx2-idx1 > cnt:
            cnt = idx2-idx1
        idx1=temp
if idx2-idx1 > cnt:
    cnt = idx2-idx1
print(cnt)
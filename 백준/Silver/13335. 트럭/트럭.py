from collections import deque
n,w,l =map(int,input().split())
al=list(map(int,input().split()))
bridge =deque([0]*w)
t=0
idx=0
cnt=0
while idx<n:
    bridge.popleft()
    if sum(bridge)+al[idx]<=l:
        bridge.append(al[idx])
        idx+=1
        t+=1
    else:
        bridge.append(0)
        t+=1
print(t+w)
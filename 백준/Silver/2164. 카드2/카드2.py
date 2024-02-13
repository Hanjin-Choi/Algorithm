import _collections
L =[x for x in range(1,int(input())+1)]
dq=_collections.deque(L)
while len(dq)>1:
    dq.popleft()
    dq.rotate(-1)
print(dq[0])
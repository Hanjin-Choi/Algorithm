from collections import deque
n=int(input())
q = deque((idx+1,num) for idx,num in enumerate((map(int,input().split()))))
while q:
    idx,num =q.popleft()
    print(idx,end=' ')
    if num >0:
        q.rotate(-num+1)
    else:
        q.rotate(-num)

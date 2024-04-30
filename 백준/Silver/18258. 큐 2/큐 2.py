import sys
input = sys.stdin.readline

from collections import deque
n=int(input())
q=deque()
for _ in range(n):
    word=input().strip()
    if 'push' in word:
        act,num=word.split()
        q.append(int(num))
    elif 'size' in word:
        print(len(q))
    elif 'empty' in word:
        if q:
            print(0)
        else:
            print(1)
    elif 'pop' in word:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'front' in word:
        if q:
            print(q[0])
        else:
            print(-1)
    else:
        if q:
            print(q[-1])
        else:
            print(-1)

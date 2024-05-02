import sys
input = sys.stdin.readline
from heapq import heappush,heappop
n= int(input())
time=[]
room=[]
for _ in range(n):
    heappush(time,list(map(int,input().strip().split())))
for _ in range(n):
    start,end =heappop(time)
    if not room:
        heappush(room, end)
        continue
    t =heappop(room)
    if t<=start:
        heappush(room,end)
    else:
        heappush(room,t)
        heappush(room,end)

print(len(room))
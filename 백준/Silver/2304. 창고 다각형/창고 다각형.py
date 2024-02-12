import sys
input = sys.stdin.readline

n=int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.sort(key=lambda x: x[0])
max_h=0
max_locate=0
max_idx =0
for idx in range(n):
    locate,h = arr[idx][0], arr[idx][1]
    if h > max_h:
        max_h = h
        max_locate = locate
        max_idx= idx
area = 0
max_left=0
left_locate=0
for left in range(max_idx+1):
    locate,h = arr[left][0], arr[left][1]
    if h>= max_left:
        area+=max_left*(locate-left_locate)
        left_locate =locate
        max_left = h
max_right=0
right_locate = 1001
for right in range(n-1,max_idx-1,-1):
    locate,h = arr[right][0], arr[right][1]
    if h>= max_right:
        area += max_right*(right_locate-locate)
        right_locate =locate
        max_right = h
area += max_h
print(area)
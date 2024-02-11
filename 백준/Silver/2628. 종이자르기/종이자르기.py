import sys
input = sys.stdin.readline

w, h = map(int,input().split())
n = int(input())
width = [0,w]
height = [0,h]
for i in range(n):
    direction, line = map(int,input().split())
    if direction == 1:
        width.append(line)
    else:
        height.append(line)
width.sort()
height.sort()
w_count=len(width)
h_count=len(height)
max_area=0
for i in range(w_count-1):
    for j in range(h_count - 1):
        area = (width[i + 1] - width[i]) * (height[j + 1] - height[j])
        if max_area < area:
            max_area =area
print(max_area)
import sys
input=sys.stdin.readline
n=int(input())
triangle=[list(map(int,input().split())) for _ in range(n)]
row=1
idx=0
height = len(triangle)
for h in range(height-2,-1,-1):
    for idx in range(h+1):
        triangle[h][idx] += max(triangle[h+1][idx],triangle[h+1][idx+1])
answer=triangle[0][0]
print(answer)
    
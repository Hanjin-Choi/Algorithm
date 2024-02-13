import sys
input = sys.stdin.readline

n=int(input())
arr = [[0]*1001 for _ in range(1001)] #빈어레이
ans=[0]*(n+1) # 답저장할 리스트

for i in range(1,n+1): # 순회
    r,c,w,h = map(int,input().split())
    for row in range(r,r+w): # 윗장면적
        for col in range(c,c+h):
            arr[row][col]=i

for i in range(1,n+1):
    for row in range(1001):
        ans[i]+=arr[row].count(i)
print(*ans[1:],sep='\n')


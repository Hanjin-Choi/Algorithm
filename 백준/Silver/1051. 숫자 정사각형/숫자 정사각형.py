import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr = [input().strip() for _ in range(n)]
ans=1
for row in range(n):
    for col in range(m):
        for i in range(1,min(n,m)):
            if row+i<n and col+i<m and arr[row][col]==arr[row+i][col]==arr[row][col+i]==arr[row+i][col+i]:
                ans = max(ans,(i+1)**2)
print(ans)
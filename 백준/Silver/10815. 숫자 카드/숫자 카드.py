import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
arr2 = list(map(int, input().split()))
ans = [0] * M
for i in range(M):
    if arr2[i] in arr:
        ans[i]=1
print(*ans)

import sys
input=sys.stdin.readline
n=int(input())
ans=-(n-1)
for _ in range(n):
    ans += int(input())
print(ans)
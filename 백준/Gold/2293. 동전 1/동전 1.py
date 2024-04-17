import sys
input=sys.stdin.readline

n,k = map(int,input().split())
coin =[int(input()) for _ in range(n)]
dp =[1]+[0]*(k)
for c in coin:
    for j in range(c,k+1):
        dp[j] +=dp[j-c]
print(dp[k])
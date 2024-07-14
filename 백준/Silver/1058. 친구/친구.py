import sys
input = sys.stdin.readline

def friend(x):
    res =0
    for idx in range(n):
        if x==idx:continue
        elif temp[x][idx]:
            res +=1
        elif f[x][idx]:
            res+=1

    return res

n=int(input())
arr=[list(input().strip()) for _ in range(n)]
temp =[[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        if arr[row][col]=='Y':
            temp[row][col]=1
        else:
            temp[row][col]=0

f=[[0]*n for _ in range(n)]
for row in range(n):
    for col in range(n):
        for i in range(n):
            f[row][col]+=temp[row][i]*temp[i][col]
ans=0
for i in range(n):
    ans=max(ans,friend(i))
print(ans)
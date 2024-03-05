import sys
input = sys.stdin.readline

n=int(input())
people =[list(map(int,input().split())) for _ in range(n)]
ans =[1]*n
for i in range(n):
    for j in range(n):
        if people[j][0]>people[i][0] and people[j][1]>people[i][1]:
            ans[i] +=1
print(*ans)
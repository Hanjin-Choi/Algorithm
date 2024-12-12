n=int(input())
lst=list(map(int,input().split()))
cnt=0
for num in lst:
    if num ==n:
        cnt+=1
print(cnt)
import sys
input = sys.stdin.readline

n,c = map(int,input().split())
lst=[int(input()) for _ in range(n)]
lst.sort()

s=1
e=lst[-1]-lst[0]
result=0
while s<=e:
    mid=(s+e)//2
    cnt=1
    location=lst[0]
    for i in range(1,n):
        if location+mid<=lst[i]:
            cnt+=1
            location=lst[i]
    if cnt>=c:
        s=mid+1
        result=mid
    else:
        e=mid-1
print(result)

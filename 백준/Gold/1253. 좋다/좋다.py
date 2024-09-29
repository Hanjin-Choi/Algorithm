import sys
input =sys.stdin.readline

n=int(input())
lst = list(map(int,input().split()))
lst.sort()
cnt=0
for i in range(n):
    start=0
    end =n-1
    while(start<end):
        res =lst[start]+lst[end]
        if (start == i):
            start +=1
        elif end==i:
            end -=1
        elif (lst[i]==res):
            cnt +=1
            break
        elif (res>lst[i]):
            end -= 1
        else:
            start += 1

print(cnt)
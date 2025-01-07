n=int(input())
cnt=1
num=10
while num<n:
    cnt += 1
    num = num+ 10**cnt
print(cnt)
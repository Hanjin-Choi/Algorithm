n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    num = arr[i][0]
    s = 0
    for j in range(1,num+1):
        s +=arr[i][j]
    s /=num
    cnt=0
    for j in range(1,num+1):
        if arr[i][j]>s:
            cnt+=1
    print(format(cnt/num*100,'.3f')+'%')

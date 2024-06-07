t=int(input())
for _ in range(t):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(2)]
    if n==1:
        ans = max(arr[0][0],arr[1][0])
    elif n==2:
        arr[0][1]+=arr[1][0]
        arr[1][1]+=arr[0][0]
        ans = max(arr[0][1],arr[1][1])
    else:
        arr[0][1] += arr[1][0]
        arr[1][1] += arr[0][0]
        idx=2
        while idx <n:
            arr[0][idx]+=max(arr[1][idx-1],arr[1][idx-2])
            arr[1][idx]+=max(arr[0][idx-1],arr[0][idx-2])
            idx+=1
        ans=max(arr[0][n-1],arr[1][n-1])
    print(ans)
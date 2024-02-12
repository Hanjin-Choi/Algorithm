n, k = map(int,input().split())
arr= list(map(int,input().split()))
ans = [0] *n
max_arr =-101*k
for i in range(n):
    if i and i <k:
        ans[i] += ans[i-1]+arr[i]
        if i ==k-1:
            max_arr = ans[i]
    elif i:
        ans[i] += ans[i-1]+arr[i]-arr[i-k]
        if max_arr < ans[i]:
            max_arr = ans[i]
    else:
        ans[i]=arr[i]
        if k==1:
            max_arr=ans[i]
print(max_arr)
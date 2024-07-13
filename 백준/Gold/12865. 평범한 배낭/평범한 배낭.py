import sys
input = sys.stdin.readline

n,k = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(n)]
arr= [[0]*(k+1) for _ in range(n)]
for idx in range(n):
    for weight in range(1,k+1):
        if idx==0 and weight >=bag[idx][0]:
            arr[0][weight]=bag[0][1]
        elif weight >=bag[idx][0]:
            arr[idx][weight]=max(arr[idx-1][weight],arr[idx-1][weight-bag[idx][0]]+bag[idx][1])
        else:
            arr[idx][weight]=arr[idx-1][weight]
print(arr[n-1][weight])
import sys
input = sys.stdin.readline

n,k = map(int,input().split())
bag = [list(map(int,input().split())) for _ in range(n)]
arr=[0]*(k+1)
for idx in range(n):
    for weight in range(k,bag[idx][0]-1,-1):
        arr[weight] =max(arr[weight-bag[idx][0]]+bag[idx][1], arr[weight])
print(arr[k])
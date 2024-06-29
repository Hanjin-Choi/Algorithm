import sys
input = sys.stdin.readline

def time(x):
    c=0
    for t in lst:
        c+=x//t
    return c
n,m = map(int,input().split())
lst=[int(input()) for _ in range(n)]
lst.sort()
start=lst[0]
end=lst[-1]*m
while start<=end:
    mid = (start+end)//2
    check = time(mid)
    if check>=m:
        end=mid -1
    else:
        start = mid +1
print(start)
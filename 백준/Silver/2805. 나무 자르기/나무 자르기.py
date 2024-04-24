def cut(mid):
    total =0
    for idx in range(n-1,-1,-1):
        if tree[idx]>mid:
            total +=tree[idx]-mid
        else:
            return total
    return total

n,m =map(int,input().split())
tree = list(map(int,input().split()))
tree.sort()
end=tree[-1]
start=0
while start<=end:
    mid=(start+end)//2
    rest = cut(mid)
    if rest < m:
        end = mid - 1
    else:
        start = mid + 1
print(end)

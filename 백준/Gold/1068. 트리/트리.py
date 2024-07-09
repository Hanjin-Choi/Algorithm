n=int(input())
adjl=[[] for _ in range(n)]
arr=list(map(int,input().split()))

def cut(a):
    if not adjl[a]:
        adjl[a].append(-1)
        return
    else:
        for idx in adjl[a]:
            cut(idx)
        adjl[a]=[-1]
        return

for i in range(n):
    if arr[i]==-1:
        continue
    adjl[arr[i]].append(i)

cnt=0
cut(int(input()))
for idx in range(n):
    if not adjl[idx]:
        cnt+=1
    elif adjl[idx][0]==-1:
        continue
    else:
        for c in adjl[idx]:
            if not adjl[c]:break
            elif adjl[c][0]!=-1:
                break
        else:
            cnt+=1

print(cnt)
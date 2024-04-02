import sys
input = sys.stdin.readline

def dfs(i):
    global maxx
    if i<n:
        breakegg=0
        for x in range(n):
            if sl[x]<=0:
                breakegg+=1
        if breakegg==n-1:
            dfs(i+1)
    if i==n:
        cnt=0
        for j in range(n):
            if sl[j]<=0:
                cnt+=1
        if maxx<cnt:
            maxx=cnt
    elif sl[i]<=0:
        dfs(i+1)
    else:
        for k in range(n):
            if i==k: continue
            elif sl[k]<=0:continue
            else:
                temp = sl[i]
                temp2=sl[k]
                sl[i]-=wl[k]
                sl[k]-=wl[i]
                dfs(i+1)
                sl[i]=temp
                sl[k]=temp2
n= int(input())
sl = [0]*n
wl = [0] *n
for idx in range(n):
    s,w = map(int,input().split())
    sl[idx]=s
    wl[idx]=w

maxx=0
dfs(0)
print(maxx)
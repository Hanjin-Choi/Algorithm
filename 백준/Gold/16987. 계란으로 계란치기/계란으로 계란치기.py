import sys
input = sys.stdin.readline

def dfs(i,breakegg):
    global maxx
    if maxx==n:
        return
    if i==n:
        if maxx<breakegg:
            maxx=breakegg
    elif sl[i]<=0:
        dfs(i+1,breakegg)
    else:
        for k in range(n):
            if i==k: continue
            elif sl[k]<=0:continue
            else:
                temp = sl[i]
                temp2=sl[k]
                sl[i]-=wl[k]
                sl[k]-=wl[i]
                wow=0
                if sl[i]<=0:
                    wow+=1
                if sl[k]<=0:
                    wow+=1
                breakegg +=wow
                dfs(i+1,breakegg)
                breakegg-=wow
                sl[i]=temp
                sl[k]=temp2
        else:
            maxx=max(breakegg,maxx)
n= int(input())
sl = [0]*n
wl = [0] *n
for idx in range(n):
    s,w = map(int,input().split())
    sl[idx]=s
    wl[idx]=w

maxx=0
dfs(0,0)
print(maxx)
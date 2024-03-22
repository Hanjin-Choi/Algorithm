from heapq import heappush,heappop
t=int(input())

def find_set(num):
    if head[num]==num:
        return num
    else:
        return find_set(head[num])
for tc in range(1,t+1):
    n=int(input())
    kruskal=[]
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    e = float(input())
    for i in range(n):
        for j in range(i):
            heappush(kruskal,(((x[j]-x[i])**2+(y[j]-y[i])**2),j,i))
    head=[i for i in range(n)]
    # visit=[0]*n
    ssum=0
    cnt=0
    while kruskal:
        dist, depart,arrive =heappop(kruskal)
        head_d = find_set(depart)
        head_a = find_set(arrive)
        if head_d==head_a: continue
        else:
            cnt+=1
            head[head_a]=head_d
            ssum+=dist*e
            if cnt == n-1:
                break
    print(f'#{tc} {ssum:.0f}')
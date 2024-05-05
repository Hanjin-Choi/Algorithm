import heapq,sys
input=sys.stdin.readline
t=int(input())
for tc in range(t):
    n=int(input())
    heap_min=[]
    heap_max=[]
    visit = [0] * n
    for idx in range(n):
        act,num=input().strip().split()
        num=int(num)
        if act=='I':
            heapq.heappush(heap_min,(num,idx))
            heapq.heappush(heap_max,(-num,idx))
            visit[idx]+=1
        elif act=='D':
            if num==-1 and heap_min:
                while heap_min:
                    temp,i = heapq.heappop(heap_min)
                    if visit[i]:
                        visit[i]-=1
                        break
            elif num==1 and heap_max:
                while heap_max:
                    temp,i = heapq.heappop(heap_max)
                    if visit[i]:
                        visit[i]-=1
                        break
    while heap_min and not visit[heap_min[0][1]]:
        mini,idx=heapq.heappop(heap_min)
    while heap_max and not visit[heap_max[0][1]]:
        maxi,idx=heapq.heappop(heap_max)
    if heap_max and heap_min:
        print(-heapq.heappop(heap_max)[0],heapq.heappop(heap_min)[0])
    else:
        print('EMPTY')

from collections import deque
def bfs(n,c):
    q=deque()
    visit[n] = 1
    q.append((n,c))
    max=[0,0]
    while q:
        num, cnt = q.popleft()
        if max[0]<cnt:
            max=[cnt,num]
        elif max[0]==cnt and max[1]<num:
            max[1]=num

        for w in adjl[num]:
            if not visit[w]:
                visit[w]=1
                q.append((w,cnt+1))
    return max[1]
for tc in range(1,11):
    length, start = map(int,input().split())
    node_list=list(map(int,input().split()))
    adjl=[set() for _ in range(101)]
    visit=[0]*101
    for idx in range(length//2):
        p,c = node_list[idx*2], node_list[idx*2+1]
        adjl[p].add(c)
    print(f'#{tc} {bfs(start,1)}')


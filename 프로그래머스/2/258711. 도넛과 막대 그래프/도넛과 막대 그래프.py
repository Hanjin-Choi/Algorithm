from collections import deque

def bfs(adjl,s):
    q=deque([s])
    visit=[0]*1000001
    donut=0
    stick=0
    eight=0
    while q:
        now=q.popleft()

        if not adjl[now]:
            stick+=1
        if now!=s and len(adjl[now])==2:
            eight +=1
            continue
        for w in adjl[now]:
            if visit[w]<=2:
                if visit[w]==2 and len(adjl[w])==1:
                    donut +=1
                else:
                    q.append(w)
                    visit[w]+=1
    return (donut,stick,eight)
def solution(edges):
    answer = []
    start=set()
    end=set()
    adjl=[set() for _ in range(1000001)]
    for s,e in edges:
        adjl[s].add(e)
        start.add(s)
        end.add(e)
    res = start-end
    for i in res:
        if len(adjl[i])>1:
            do,st,egt =bfs(adjl,i)
            answer=[i,do,st,egt]
    return answer
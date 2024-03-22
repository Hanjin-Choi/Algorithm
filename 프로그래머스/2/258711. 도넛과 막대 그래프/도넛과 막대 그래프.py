def solution(edges):
    answer = []
    start=set()
    end=set()
    eight=set()
    maxx=0
    for i in edges:
        maxx=max(maxx,i[0],i[1])
    print(maxx)
    adjl=[set() for _ in range(maxx+1)]
    for s,e in edges:
        adjl[s].add(e)
        start.add(s)
        end.add(e)
        if len(adjl[s])==2:
            eight.add(s)
    stick=len(end-start)
    res = eight-end
    for i in res:
        graph=len(adjl[i])
        ecount=len(eight-{i})
        answer=[i,graph-stick-ecount,stick,ecount]
    return answer
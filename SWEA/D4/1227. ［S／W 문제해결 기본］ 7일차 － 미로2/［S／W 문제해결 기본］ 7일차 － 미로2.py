def find(arr,n):
    for i in range(n):
        for j in range(n):
            if arr[i][j]==2:
                start= [i,j]
            elif arr[i][j]==3:
                end= [i,j]
    return [start,end]
def bfs(arr,n):
    s,e=find(arr,n)
    queue = []
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    s +=[0]
    queue.append(s)
    while queue:
        ppop = queue.pop(0)
        row = ppop[0]
        col = ppop[1]
        for i in range(4):
            rr = row+dr[i]
            cc = col+dc[i]
            if 0<=rr<n and 0<=cc<n and arr[rr][cc]==0:
                arr[rr][cc]=1
                queue.append([rr,cc])
            elif rr==e[0] and cc==e[1]:
                return 1
    return 0
T=10
for tc in range(1, T+1):
    t=int(input())
    n=100
    arr= [list(map(int,list(input()))) for _ in range(n)]
    print(f'#{tc} {bfs(arr, n)}')

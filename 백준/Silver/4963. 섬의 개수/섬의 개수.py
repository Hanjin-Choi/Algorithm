from collections import deque
def bfs(r,c,w,h,arr):
    q=deque()
    q.append((r,c))
    while q:
        now_r,now_c = q.popleft()
        for dr,dc in [(1,0),(0,1),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            rr= now_r+dr
            cc=now_c+dc
            if 0<=rr<h and 0<=cc<w and arr[rr][cc] and not visit[rr][cc]:
                visit[rr][cc]=1
                q.append((rr,cc))
    return 1

while True:
    w,h = map(int,input().split())
    if w==h==0:
        break
    arr = [list(map(int,input().split())) for _ in range(h)]
    visit= [[0]*w for _ in range(h)]
    cnt =0

    for row in range(h):
        for col in range(w):
            if not visit[row][col] and arr[row][col]:
                cnt += bfs(row,col,w,h,arr)
    print(cnt)
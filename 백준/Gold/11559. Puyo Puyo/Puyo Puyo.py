from collections import deque
dm=[(0,1),(1,0),(0,-1),(-1,0)]
def comp(r,c):
    temp = arr[r][c]
    q=deque([(r,c)])
    visit[r][c]=1
    cnt = 1
    while q:
        row,col = q.popleft()
        for i in range(4):
            rr = row + dm[i][0]
            cc = col + dm[i][1]
            if 0<=rr<12 and 0<=cc<6 and arr[rr][cc]==temp and not visit[rr][cc]:
                cnt+=1
                q.append((rr,cc))
                visit[rr][cc]=1
    if cnt>=4:
        return 1
    else:
        return 0


def boom(r,c):
    q=deque([(r,c)])
    if comp(r,c):
        temp=arr[r][c]
        arr[r][c]='.'
        while q:
            row,col = q.popleft()
            for i in range(4):
                rr = row + dm[i][0]
                cc = col + dm[i][1]
                if 0 <= rr < 12 and 0 <= cc < 6 and visit[rr][cc] and temp == arr[rr][cc]:
                    q.append((rr, cc))
                    arr[rr][cc]='.'
                    visit[rr][cc] = 0
        return 1
    else:
        return 0

def arrange():
    temp=[['.']*6 for _ in range(12)]
    for col in range(6):
        r=11
        for row in range(11,-1,-1):
            if arr[row][col]=='.':continue
            else:
                temp[r][col]=arr[row][col]
                r-=1
    return temp
arr=[list(input()) for _ in range(12)]
ans=0
while True:
    flag=0
    visit = [[0]*6 for _ in range(12)]
    for row in range(11,-1,-1):
        for col in range(6):
            if arr[row][col]=='.':continue
            else:
                flag+=boom(row,col)
    if not flag:
        break
    ans+=1
    arr=arrange()
print(ans)
import sys
input = sys.stdin.readline
dr=[1,-1,0,0]
dc=[0,0,1,-1]

def changearr():
    for many in range(4,-1,-1):
        for blk in range(4,-1,-1):
            if status[many][blk]:
                rr,cc=status[many][blk][0]
                arr[rr][cc]=s
                return
def sum_happy():
    total =0
    for row in range(n):
        for col in range(n):
            cnt =0
            for i in range(4):
                r=row+dr[i]
                c=col + dc[i]
                if 0<=r<n and 0<=c<n and arr[r][c] in like_friend[arr[row][col]]:
                    cnt +=1
            if cnt>0:
                total += 10**(cnt-1)
    return total

def make_status():
    for row in range(n):
        for col in range(n):
            if not arr[row][col]:
                cnt=0
                blank=0
                for i in range(4):
                    r=row+dr[i]
                    c=col+dc[i]
                    if 0<=r<n and 0<=c<n:
                        if arr[r][c] in ls:
                            cnt+=1
                        elif not arr[r][c]:
                            blank +=1
                status[cnt][blank].append((row,col))


n=int(input())
arr = [[0]*n for _ in range(n)]
like_friend= [0]*(n**2+1)
for _ in range(n**2):
    s,*ls =map(int,input().split())
    ls=set(ls)
    like_friend[s]=ls
    status=[[[] for _ in range(5)] for _ in range(5)]
    make_status()
    changearr()
print(sum_happy())

import sys
input = sys.stdin.readline
def countzo(i,j,n):
    one=zero=0
    for r in range(i,i+n):
        for c in range(j,j+n):
            if arr[r][c]:
                one +=1
            else:
                zero +=1
    return one,zero

def bw(r,c,n):
    global blue,white
    one,zero = countzo(r,c,n)
    if not one:
        white +=1
        return
    elif not zero:
        blue +=1
        return
    else:
        bw(r,c,n//2)
        bw(r,c+n//2,n//2)
        bw(r+n//2,c,n//2)
        bw(r+n//2,c+n//2,n//2)

n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
blue=0
white=0
bw(0,0,n)
print(white)
print(blue)
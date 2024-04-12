import sys
input = sys.stdin.readline

def countzo(i,j,n):
    one=zero=0
    for r in range(i,i+n):
        for c in range(j,j+n):
            if arr[r][c]=='1':
                one +=1
            else:
                zero +=1
    return one,zero

def makecode(r,c,n):
    one,zero=countzo(r,c,n)
    if not one:
        return '0'
    elif not zero:
        return '1'
    else:
        return '('+makecode(r,c,n//2)+makecode(r,c+n//2,n//2)+makecode(r+n//2,c,n//2)+makecode(r+n//2,c+n//2,n//2)+')'
n=int(input())
arr=[list(input()) for _ in range(n)]
print(makecode(0,0,n))
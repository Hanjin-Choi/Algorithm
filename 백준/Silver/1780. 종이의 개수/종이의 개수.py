n=int(input())

arr= [list(map(int,input().split())) for _ in range(n)]
zero=0
one=0
mone=0
def find(n,r,c):
    global zero,one,mone
    temp = arr[r][c]
    flag=0
    for a in range(r,r+n):
        for b in range(c,c+n):
            if temp !=arr[a][b]:
                flag=1
                break
        if flag:
            break
    if flag:
        for rr in range(r,r+n,n//3):
            for cc in range(c,c+n,n//3):
                find(n//3,rr,cc)
    else:
        if temp==0:
            zero +=1
        elif temp==1:
            one+=1
        elif temp==-1:
            mone+=1
    return

find(n,0,0)

print(mone)
print(zero)
print(one)


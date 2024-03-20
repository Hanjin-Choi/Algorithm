import sys
input = sys.stdin.readline

def make_tri(num):
    tri=['']*num
    if num==3:
        return['  *  ',' * * ','*****']
    else:
        base = make_tri(num//2)
        for i in range(num-1,-1,-1):
            if i>=num//2:
                tri[i]=base[i-num//2]+' '+base[i-num//2]
            else:
                tri[i]=' '*(num//2)+base[i]+' '*(num//2)
        return tri
n=int(input())
res=make_tri(n)
print(*res,sep='\n')
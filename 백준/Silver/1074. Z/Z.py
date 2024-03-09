

def z(n,start,r,c,row,col):
    if n==1:
        if r==row and c==col:
            return start
        elif r==row and c+1 ==col:
            return start+1
        elif r+1==row and c==col:
            return start+2
        elif r+1==row and c+1==col:
            return start+3
        return
    else:
        if r<=row< r+2 ** (n - 1) and c<=col<c+2 ** (n - 1):
            r1=z(n - 1, start, r, c,row,col)
            if r1: return r1
        elif r<=row<r+2 ** (n - 1) and c+2 ** (n - 1)<=col<c+2**n:
            r2=z(n - 1, start + 2 ** (2 * n - 2), r , c+ 2 ** (n - 1),row,col)
            if r2: return r2
        elif r+2 ** (n - 1)<=row<r+2**n and c<=col<c+2 ** (n - 1):
            r3=z(n - 1, start + (2 ** (2 * n - 2))*2, r + 2 ** (n - 1), c,row,col)
            if r3: return r3
        else:
            r4=z(n - 1, start + (2 ** (2 * n - 2))*3, r + 2 ** (n - 1), c+ 2 ** (n - 1),row,col)
            if r4:return r4
        return
n,r,c = map(int,input().split())
ans=z(n,0,0,0,r,c)

print(ans)




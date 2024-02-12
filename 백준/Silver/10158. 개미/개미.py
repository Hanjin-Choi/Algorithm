import sys
input = sys.stdin.readline
def gcd(a,b): # 유클리드 호제법
    if a>=b:
        d,m = divmod(a,b)
        if m:
            g=gcd(b,m)
        else:
            return b
    else:
        d,m = divmod(b,a)
        if m:
            g=gcd(a,m)
        else:
            return a
    return g
w,h=map(int,input().split())
x,y = map(int,input().split())
t=int(input())
gcd=gcd(w,h)
lcm = w*h//gcd
rest_move = t%(2*lcm)
dx=1
dy=1
rest_x =rest_move%(2*w)
rest_y = rest_move%(2*h)
if x + rest_x <= w:
    x +=rest_x
elif w<x+ rest_x<=2*w:
    x = w-(rest_x+x-w)
elif 2*w<x+rest_x:
    x += rest_x - 2*w
if y + rest_y <= h:
    y += rest_y
elif h < y + rest_y <= 2 * h:
    y = h - (rest_y + y - h)
elif 2 * h < y + rest_y:
    y += rest_y - 2 * h
print(x,y)
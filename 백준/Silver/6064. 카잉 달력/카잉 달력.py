import sys
input = sys.stdin.readline

def uclid(m, n):
    if m < n:
        m, n = n, m
    elif m == n:
        return m

    while True:
        d, k = divmod(m, n)
        if k == 0:
            return n
        else:
            m, n = n, k


t = int(input())
for tc in range(t):
    m, n, x, y = map(int, input().split())
    gcd = uclid(m, n)
    lcm = m * n // gcd
    lst=set()
    while x<=lcm:
        lst.add(x)
        x+=m
    while y <= lcm:
        if y in lst:
            break
        else:
            y+=n
    if y > lcm:
        print(-1)
    else:
        print(y)

try:
    while True:
        n, k = map(int, input().split())
        m = n
        while m > 0:
            m, r = divmod(m, k)
            if m==0:
                break
            n += m
            m += r
        print(n)
except:
    exit()
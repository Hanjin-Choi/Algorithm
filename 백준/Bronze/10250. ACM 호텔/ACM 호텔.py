test_case = int(input())
for test in range(test_case):
    h,w,n = map(int,input().split())
    d, m = divmod(n,h)

    if m ==0:
        m=h
    else:
        d= d+1
        m= m
    print(f'{m}{d:02d}')
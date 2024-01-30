t = int(input())
for case in range(t):
    A, B = map(int, input().split())
    a, b = max(A,B), min(A,B)
    # 유클리드 호제법 사용(큰수를 작은수로 나누었을 때, 나누어 떨이지면 그수가 최대공약수)
    m=1
    while m != 0:
        d,m = divmod(a,b)
        a,b = b,m
    print(A*B//a)
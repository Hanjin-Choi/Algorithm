T = int(input())
for i in range(T):
    Q, r = divmod(int(input()),25)
    D, r = divmod(r,10)
    N, P = divmod(r,5)
    print(Q,D,N,P)
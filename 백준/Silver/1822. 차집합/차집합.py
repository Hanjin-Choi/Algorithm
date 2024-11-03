a,b=map(int,input().split())
A=set(list(map(int,input().split())))
B=set(list(map(int,input().split())))
S=A-B
S=list(S)
if len(S):
    print(len(S))
    S.sort()
    print(*S)
else:
    print(0)

n, m = map(int, input().split())
pd = {}
for i in range(1, n + 1):
    poke = input()
    pd.setdefault(poke, i)
    pd.setdefault(str(i),poke)
    
for j in range(m):
    print(pd[input()])

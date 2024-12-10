ans=[1]*251
ans[1]=1
ans[2]=3
for i in range(3,251):
    ans[i]=ans[i-1]+ans[i-2]*2
while True:
    try:
        n=int(input())
        print(ans[n])
    except EOFError:
        break
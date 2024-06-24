n=int(input())
lst = [input() for _ in range(n)]
leng=-1
while True:
    s=set()
    for i in range(n):
        if lst[i][leng::] not in s:
            s.add(lst[i][leng::])
        else:
            break
    else:
        break
    leng-=1
print(-leng)
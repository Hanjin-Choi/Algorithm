t=int(input())
def combi(i,c):
    global mini
    if b+mini>c>=b:
        mini= c-b
        return
    elif c>=b+mini:
        return
    elif i==n:
        return
    else:
        combi(i+1,c+nl[i])
        combi(i+1,c)
for tc in range(1,t+1):
    n,b = map(int,input().split())
    nl= list(map(int,input().split()))
    nl.sort(reverse=True)
    mini=b
    combi(0,0)
    print(f'#{tc} {mini}')
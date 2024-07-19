def back(c):
    global cnt
    if c==n:
        cnt+=1
        return
    else:
        for i in range(n):
            visit[c]=i
            if check(c):
                back(c+1)


def check(c):
    for i in range(c):
        if visit[c]==visit[i] or c-i==abs(visit[c]-visit[i]):
            return False
    return True
n=int(input())
visit = [0]*n
cnt=0
for i in range(n):
    visit[0]=i
    back(1)
print(cnt)
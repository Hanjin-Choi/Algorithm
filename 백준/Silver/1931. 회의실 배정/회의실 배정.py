import sys
input = sys.stdin.readline

n=int(input())
li=[list(map(int,input().split())) for _ in range(n)]
li.sort(key=lambda x: (x[1],x[0]))
c=0
finish=0
for l in li:
    if l[0]>=finish:
        c+=1
        finish=l[1]
print(c)
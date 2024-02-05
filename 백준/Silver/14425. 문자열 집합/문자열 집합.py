import sys
input= sys.stdin.readline

n,m =map(int,input().split())
set_word={input() for _ in range(n)}
compare =[input() for _ in range(m)]
c=0
for word in compare:
    if word in set_word:
        c+=1
print(c)
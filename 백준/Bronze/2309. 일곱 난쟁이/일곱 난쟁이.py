import sys
input = sys.stdin.readline

l = [int(input()) for _ in range(9)]
l.sort()

search=sum(l)-100
for i in range(8,-1,-1):
    s =search
    s -= l[i]
    if s in l:
        l.remove(l[i])
        l.remove(s)
        break
print(*l, sep='\n')
import sys
input = sys.stdin.readline

n=int(input())
s=set()
cnt=0
for _ in range(n):
    l=input().strip()
    if l == 'ENTER':
        cnt+=len(s)
        s=set()
    elif l in s:
        continue
    elif l not in s:
        s.add(l)
cnt+=len(s)
print(cnt)

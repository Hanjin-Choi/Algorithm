import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
l.sort()
suml=1
for i in range(0,n):
    if l[i]>suml:
        break
    suml += l[i]
print(suml)
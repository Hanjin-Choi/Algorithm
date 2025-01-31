import sys
input=sys.stdin.readline
n=int(input())

for _ in range(n):
    s= int(input())
    if s&(-s)==s:
        print(1)
    else:
        print(0)
import sys
input = sys.stdin.readline

N = int(input())
NL = set(map(int,input().split()))
M = int(input())
ML= list(map(int,input().split()))
for j in ML:
    if j in NL:
        print(1)
    else:
        print(0)
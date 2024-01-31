import sys
N= int(sys.stdin.readline())
L=[0]*10001
for i in range(1,N+1):
    L[int(sys.stdin.readline())]+=1
for j in range(1,10001):
    for k in range(L[j]):
        print(j)
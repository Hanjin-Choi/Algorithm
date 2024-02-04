import sys
input = sys.stdin.readline

K, N = map(int,input().split())
L = [0]*K
s =0
for i in range(K):
    L[i] = int(input())
    s +=L[i]
end = s//N
start =s//(N+K)+1
num =0

while start<=end:
    num =0
    middle = (start+end)//2
    for i in range(K):
        a = L[i]//middle
        num += a
    if num>=N:
        start = middle + 1
    else:
        end = middle - 1
print(end)
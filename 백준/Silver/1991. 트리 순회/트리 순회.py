import sys
input = sys.stdin.readline

def pre(n):
    print(rev[n],end='')
    if adjl[n][0]>-1:
        pre(adjl[n][0])
    if adjl[n][1]>-1:
        pre(adjl[n][1])

def inorder(n):
    if adjl[n][0] > -1:
        inorder(adjl[n][0])
    print(rev[n], end='')
    if adjl[n][1] > -1:
        inorder(adjl[n][1])

def post(n):
    if adjl[n][0] > -1:
        post(adjl[n][0])
    if adjl[n][1] > -1:
        post(adjl[n][1])
    print(rev[n], end='')

n=int(input())
adjl=[[] for _ in range(n)]
alpha ={chr(i+65):i for i in range(n)}
rev = {i:chr(i+65) for i in range(n)}
for _ in range(n):
    p, c1,c2 = input().strip().split()
    if c1=='.':
        adjl[alpha[p]].append(-1)
    else:
        adjl[alpha[p]].append(alpha[c1])
    if c2 =='.':
        adjl[alpha[p]].append(-1)
    else:
        adjl[alpha[p]].append(alpha[c2])
pre(0)
print()
inorder(0)
print()
post(0)

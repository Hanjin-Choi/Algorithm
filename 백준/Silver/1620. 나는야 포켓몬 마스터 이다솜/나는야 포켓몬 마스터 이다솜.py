import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pd = {}
for i in range(1, n + 1):
    poke = input().rstrip()
    pd[poke]=i
    pd[str(i)]=poke

for j in range(m):
    print(pd[input().rstrip()])
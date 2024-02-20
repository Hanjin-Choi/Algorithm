import sys
input = sys.stdin.readline
n= int(input())
l = [int(input().rstrip()) for _ in range(n)]
l.sort()
ans = '\n'.join(map(str,l))
print(ans)

n=int(input())
for _ in range(n):
    lst = list(input().split())
    new = lst[2:]+lst[:2]
    print(*new)
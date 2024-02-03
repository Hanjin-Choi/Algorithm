import sys
input = sys.stdin.readline

N, d, k, c = map(int,input().split())
L = [0]*N*2
for x in range(N):
    L[x] =int(input())
    L[N+x] =L[x]
max_kind = 0
for dish_num in range(N):
    a=L[dish_num:dish_num+k]+[c]
    if max_kind < len(set(L[dish_num:dish_num +k]+[c])):
        max_kind =len(set(L[dish_num:dish_num +k]+[c]))

print(max_kind)
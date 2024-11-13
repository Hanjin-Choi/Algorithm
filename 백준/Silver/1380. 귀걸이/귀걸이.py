cnt=0
while True:
    n = int(input())
    cnt+=1
    if n == 0:
        break
    name = [input() for _ in range(n)]
    num = [3] * n

    for _ in range(2 * n - 1):
        i, act = input().split()
        if act == 'A':
            num[int(i) - 1] -= 1
        else:
            num[int(i) - 1] -= 2
    for idx in range(n):
        if num[idx]:
            print(cnt, name[idx])
            break

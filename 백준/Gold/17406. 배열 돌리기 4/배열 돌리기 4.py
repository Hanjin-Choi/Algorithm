import sys

input = sys.stdin.readline

dm = [(0, 1), (1, 0), (0, -1), (-1, 0)]
def turn(r, c, s,arr2):
    temp = [[0] * m for _ in range(n)]
    temp[r][c] = arr2[r][c]
    for row in range(n):
        for col in range(m):
            if r - s <= row <= r + s and c - s<= col <= c + s and not temp[row][col]:
                rr = row
                cc = col
                for i in range(4):
                    while True:
                        if r - s <= rr + dm[i][0] <= r + s and c - s<= cc + dm[i][1] <= c + s and not temp[rr + dm[i][0]][cc + dm[i][1]]:
                            t = arr2[rr][cc]
                            rr += dm[i][0]
                            cc += dm[i][1]
                            temp[rr][cc] = t
                        else:
                            break
            elif not temp[row][col]:
                temp[row][col] = arr2[row][col]
    return temp

def perm(cnt):
    global mini
    if cnt==k:
        arr2=[arr[l][:] for l in range(n)]
        for idx in range(k):
            r,c,s = lst[perms[idx]]
            arr2=turn(r-1,c-1,s,arr2)
        for row in range(n):
            res = sum(arr2[row])
            if res < mini:
                mini = res
    else:
        for i in range(cnt,k):
            perms[cnt],perms[i] =perms[i],perms[cnt]
            perm(cnt+1)
            perms[cnt], perms[i] = perms[i], perms[cnt]
n, m, k = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
lst=[tuple(map(int,input().split())) for _ in range(k)]
perms=[i for i in range(k)]
mini = 100 * m
perm(0)

print(mini)
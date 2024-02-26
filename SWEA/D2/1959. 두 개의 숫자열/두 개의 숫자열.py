t=int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    nl = list(map(int,input().split()))
    ml = list(map(int,input().split()))
    if n >=m:
        for i in range(n-m+1):
            temp =0
            for j in range(m):
                temp += nl[j+i]*ml[j]
            if i ==0:
                max_sum =temp
            if temp > max_sum:
                max_sum = temp
    else:
        for i in range(m-n+1):
            temp = 0
            for j in range(n):
                temp += nl[j] * ml[j+i]
            if i == 0:
                max_sum = temp
            if temp > max_sum:
                max_sum = temp
    print(f'#{tc} {max_sum}')
from math import factorial
def backt(c,ls,s):
    global cnt
    if c==n and ls>=s-ls:
        cnt+=1
        return
    elif ls<s-ls:
        return
    elif ls >=w_sum-ls:
        cnt += 2**(n-c) * factorial(n-c)
        return
    else:
        for idx in range(c,n):
            w_list[c], w_list[idx] = w_list[idx],w_list[c]
            backt(c + 1, ls + w_list[c], s + w_list[c])
            if c>0 and ls >=w_list[c]:
                backt(c + 1, ls,s+w_list[c])
            w_list[c], w_list[idx] = w_list[idx], w_list[c]




t= int(input())
for tc in range(1,t+1):
    n = int(input())
    w_list = list(map(int,input().split()))
    w_sum =sum(w_list)
    # cnt =[set() for _ in range(w_sum+1)]
    cnt =0
    backt(0,0,0)
    print(f'#{tc} {cnt}')
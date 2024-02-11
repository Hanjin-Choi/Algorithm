import sys
input = sys.stdin.readline

t= int(input())
for i in range(t):
    n, q = map(int,input().split())
    arr = list(map(int,input().split()))
    sequence =arr[:]
    sequence.sort(reverse=True)
    print_num = 0
    count_num = 0
    que = arr*n
    for j in range(n**2):
        if que[j] == sequence[print_num]:
            if j <n**2-n:
                que[j+n]=0
            print_num +=1
            count_num +=1
            if j ==q:
                break
        else:
            if j<n**2-n:
                que[j+n]=que[j]
                if j==q:
                    q += n
    print(count_num)

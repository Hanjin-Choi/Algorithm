N,K = map(int,input().split())
num_list = [x for x in range(2,N+1)]
while K>0:
    sosu = num_list[0]
    for num in num_list:
        if num % sosu ==0:
            num_list.remove(num)
            K -=1
            if K==0:
                break
print(num)
import sys
input = sys.stdin.readline

N = int(input())
arr = [0,0] + [1]*(N-1)
prime=[]
for i in range(2,N+1):
    if arr[i]:
        prime.append(i)
        for j in range(i*2,N+1,i):
            arr[j] =0
sum_num =0
j=0
k=0
count_num = 0
while sum_num<N and j <len(prime):
    sum_num+=prime[j]
    j+=1
    if sum_num == N and j!=len(prime):
        count_num += 1
        sum_num -= prime[k]
        k +=1
    elif sum_num>N:
        while sum_num>N:
            sum_num -=prime[k]
            k +=1
            if sum_num==N and j!=len(prime):
                count_num += 1
                sum_num -= prime[k]
                k += 1
if sum_num == N:
    count_num +=1


print(count_num)
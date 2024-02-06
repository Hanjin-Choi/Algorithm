import sys
input = sys.stdin.readline
T = int(input())
input_list = [int(input()) for _ in range(T)]
max_num = max(input_list)
L =[0]+[1]*max_num
for i in range(2,max_num+1):
    for j in range(i,max_num+1,i):
        L[j] += i
    L[i]+=L[i-1]
for k in input_list:
    print(L[k])
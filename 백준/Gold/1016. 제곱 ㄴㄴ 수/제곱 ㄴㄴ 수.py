import math, sys
input = sys.stdin.readline

min_num, max_num = map(int,input().split())
arr = [1]*(max_num-min_num+1)
max_search=int(math.sqrt(max_num)) + 1
min_search=int(math.sqrt(min_num)) + 1 # 2부터 민서치까지 먼저 제거를 해야
for square in range(2, max_search):
    d=min_num //(square**2)
    for i in range(d*(square**2),max_num+1,square**2):
        if min_num<=i<=max_num and arr[i-min_num]:
            arr[i-min_num]=0
print(sum(arr))
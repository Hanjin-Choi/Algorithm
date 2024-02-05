import sys
input = sys.stdin.readline

N = int(input())
big_arr =[list(map(int,input().split())) for _ in range(N)]
arr=big_arr[N-2][:]
for row in range(N-2, -1,-1):
    for col in range(3):
        temp = 1000*N
        for col_1 in range(3):
            if col != col_1 and big_arr[row][col]+big_arr[row+1][col_1]<temp:
                temp = big_arr[row][col]+big_arr[row+1][col_1]
        big_arr[row][col]=temp
print(min(big_arr[0]))
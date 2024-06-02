def solution(m, n, puddles):
    arr = [[0]*m for _ in range(n)]
    for row in range(n):
        for col in range(m):
            if row==0 and col==0:
                arr[row][col]=1
            elif [col+1,row+1] in puddles:
                arr[row][col]=0
            elif row==0:
                arr[row][col]=arr[row][col-1]
            elif col==0:
                arr[row][col]=arr[row-1][col]
            else:
                arr[row][col]=arr[row][col-1]+arr[row-1][col]
    answer = arr[n-1][m-1]%1000000007            
    return answer
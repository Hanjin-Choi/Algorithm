import sys
input = sys.stdin.readline

def mul(x):
    if x==1:
        ans=[[0]*n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                ans[row][col] = arr[row][col]%1000
        return ans
    elif x%2:
        temp = mul(x//2)
        ans = [[0]*n for _ in range(n)]
        ans2=[[0]*n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                for i in range(n):
                    ans[row][col]+=temp[row][i]*temp[i][col]
                ans[row][col] %=1000
        for row in range(n):
            for col in range(n):
                for i in range(n):
                    ans2[row][col] += ans[row][i] * arr[i][col]
                ans2[row][col] %= 1000
        return ans2
    else:
        temp = mul(x // 2)
        ans = [[0] * n for _ in range(n)]
        for row in range(n):
            for col in range(n):
                for i in range(n):
                    ans[row][col] += temp[row][i] * temp[i][col]
                ans[row][col] %= 1000
        return ans


n,b=map(int,input().split())
arr= [list(map(int,input().split())) for _ in range(n)]
res= mul(b)
for row in range(n):
    print(' '.join(map(str,res[row])))

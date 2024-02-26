t= int(input())

for tc in range(1,t+1):
    n,m = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(n)]
    di=[-1,0,1]
    count_point=0
    for row in range(n):
        for col in range(m):
            count_low =0
            for r in range(3):
                for c in range(3):
                    rr=row+di[r]
                    cc=col+di[c]
                    if 0<=rr<n and 0<=cc<m and arr[rr][cc]<arr[row][col]:
                        count_low +=1
            if count_low >=4:
                count_point+=1


    print(f'#{tc} {count_point}')
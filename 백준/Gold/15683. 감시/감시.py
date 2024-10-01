import sys
input = sys.stdin.readline

di = [(-1,0),(0,1),(1,0),(0,-1)]

watch = [] # CCTV 위치 담기
def check_cctv(): # CCTV 위치 확인 및 보이는 위치를 체크
    for row in range(n):
        for col in range(m):
            if not arr[row][col]:
                continue
            elif arr[row][col]==6:
                temp= set()
                temp.add((row,col))
                watch.append(((row,col),[temp]))
                continue
            elif arr[row][col]:
                lst_watch = check_tile(arr[row][col],row,col)
                watch.append(((row,col),lst_watch))
def check_tile(num,row_cctv,col_cctv):
    lst =[]
    if num ==1:
        for idx in range(4):
            can_watch = set()
            can_watch.add((row_cctv, col_cctv))
            row = row_cctv
            col = col_cctv
            while (0 <= row < n and 0 <= col < m and arr[row][col] != 6):
                row += di[idx][0]
                col += di[idx][1]
                if 0<=row<n and 0<=col<m and arr[row][col] !=6:
                    can_watch.add((row,col))
            lst.append(can_watch)

    elif num ==2:
        for idx in range(2):
            can_watch =set()
            can_watch.add((row_cctv, col_cctv))
            first_row= second_row = row_cctv
            first_col= second_col = col_cctv
            while (0<=first_row<n and 0<=first_col<m and arr[first_row][first_col] !=6):
                first_row +=di[idx][0]
                first_col += di[idx][1]
                if 0<=first_row<n and 0<=first_col<m and arr[first_row][first_col] !=6:
                    can_watch.add((first_row,first_col))
            while (0 <= second_row < n and 0 <= second_col < m and arr[second_row][second_col] !=6):
                second_row += di[idx+2][0]
                second_col += di[idx+2][1]
                if 0 <= second_row < n and 0 <= second_col < m and arr[second_row][second_col] !=6:
                    can_watch.add((second_row,second_col))
            lst.append(can_watch)

    elif num == 3:
        for idx in range(4):
            can_watch = set()
            can_watch.add((row_cctv, col_cctv))
            first_row= second_row = row_cctv
            first_col= second_col = col_cctv
            while (0 <= first_row < n and 0 <= first_col < m and arr[first_row][first_col] !=6):
                first_row += di[idx][0]
                first_col += di[idx][1]
                if 0 <= first_row < n and 0 <= first_col < m and arr[first_row][first_col] !=6:
                    can_watch.add((first_row, first_col))

            while (0 <= second_row < n and 0 <= second_col < m and arr[second_row][second_col] !=6):
                second_row += di[(idx+1)%4][0]
                second_col += di[(idx+1)%4][1]
                if 0 <= second_row < n and 0 <= second_col < m and arr[second_row][second_col] !=6:
                    can_watch.add((second_row, second_col))
            lst.append(can_watch)

    elif num == 4:
        for idx in range(4):
            can_watch = set()
            can_watch.add((row_cctv, col_cctv))
            first_row=second_row=third_row = row_cctv
            first_col=second_col=third_col = col_cctv
            while (0 <= first_row < n and 0 <= first_col < m and arr[first_row][first_col] !=6):
                first_row += di[idx][0]
                first_col += di[idx][1]
                if 0 <= first_row < n and 0 <= first_col < m and  arr[first_row][first_col] !=6:
                    can_watch.add((first_row, first_col))
            while (0 <= second_row < n and 0 <= second_col < m and arr[second_row][second_col] !=6):
                second_row += di[(idx + 1) % 4][0]
                second_col += di[(idx + 1) % 4][1]
                if 0 <= second_row < n and 0 <= second_col < m and arr[second_row][second_col] !=6:
                    can_watch.add((second_row, second_col))
            while (0 <= third_row < n and 0 <= third_col < m and arr[third_row][third_col] != 6):
                third_row += di[(idx - 1) % 4][0]
                third_col += di[(idx - 1) % 4][1]
                if 0 <= third_row < n and 0 <= third_col < m and arr[third_row][third_col] != 6:
                    can_watch.add((third_row,third_col))
            lst.append(can_watch)

    elif num ==5:
        can_watch = set()
        can_watch.add((row_cctv, col_cctv))
        for idx in range(4):
            row = row_cctv
            col = col_cctv
            while (0<=row<n and 0<=col<m and arr[row][col] !=6):
                row +=di[idx][0]
                col += di[idx][1]
                if 0<=row<n and 0<=col<m and arr[row][col] !=6:
                    can_watch.add((row,col))
        lst.append(can_watch)
    return lst

def count_watch(i):
    global ans
    if i ==leng:
        temp =set()
        for idx in range(leng):
            value = res[idx]
            temp |= watch[idx][1][value]
        total = n*m - len(temp)
        if ans > total:
            ans =total
            return
    else:
        dir = len(watch[i][1])
        for x in range(dir):
            res[i]= x
            count_watch(i+1)
            res[i]=-1

n,m = map(int,input().split())
arr =[list(map(int,input().split())) for _ in range(n)]

ans =n*m
check_cctv()
leng = len(watch)
res = [-1]*leng
count_watch(0)
print(ans)
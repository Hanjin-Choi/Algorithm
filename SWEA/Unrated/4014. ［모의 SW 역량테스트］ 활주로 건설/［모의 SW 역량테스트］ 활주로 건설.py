t=int(input())

for tc in range(1,t+1):
    n,x = map(int,input().split())
    arr =[list(map(int,input().split())) for _ in range(n)]
    count_flag=2*n
    for row in range(n):
        flag_row=0 #올라가기
        flag_col=0
        road_row = 1
        road_col = 1
        for col in range(n):
            if flag_row !=1:
                if 0<col and arr[row][col-1]==arr[row][col]:
                    road_row +=1
                    if col==n-1 and road_row<x and flag_row==0.5:
                        flag_row=1
                elif 0 < col and arr[row][col - 1] + 1 == arr[row][col]:
                    if road_row<x:
                        flag_row=1
                    elif flag_row ==0.5 and road_row<2*x:
                        flag_row=1
                    else:
                        road_row = 1
                        flag_row =0
                elif 0 < col and arr[row][col - 1] + 1 < arr[row][col]:
                    flag_row =1
                elif 0 < col and arr[row][col - 1] - 1 == arr[row][col]:
                    if road_row < x and flag_row == 0.5:
                        flag_row = 1
                    else:
                        road_row = 1
                        flag_row = 0.5  # 내려가기
                elif 0 < col and arr[row][col - 1] -1 > arr[row][col]:
                    flag_row = 1

            if flag_col !=1:
                if 0<col and arr[col-1][row]==arr[col][row]:
                    road_col +=1
                    if col==n-1 and road_col<x and flag_col==0.5:
                        flag_col=1
                elif 0 < col and arr[col-1][row] + 1 == arr[col][row]:
                    if road_col<x:
                        flag_col=1
                    elif flag_col ==0.5 and road_col<2*x:
                        flag_col=1
                    else:
                        road_col = 1
                        flag_col =0
                elif 0 < col and arr[col - 1][row] + 1 < arr[col][row]:
                    flag_col =1
                elif 0 < col and arr[col-1][row] - 1 == arr[col][row]:
                    if road_col < x and flag_col == 0.5:
                        flag_col = 1
                    else:
                        road_col = 1
                        flag_col = 0.5
                elif 0 < col and arr[col-1][row] - 1 > arr[col][row]:
                    flag_col = 1


        if flag_row == 0.5 and road_row<x :
            flag_row=1
        if flag_col ==0.5 and road_col<x:
            flag_col =1
        if flag_row==1:
            count_flag -=1
        if flag_col==1:
            count_flag -=1

    print(f'#{tc} {count_flag}')
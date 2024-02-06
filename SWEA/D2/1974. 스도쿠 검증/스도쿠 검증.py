
T=int(input())
for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    total = 0
    for row in range(9):

        count_row = 0
        count_col = 0

        count_rarr = [1]*10
        count_carr = [1]*10

        for col in range(9):
            count_nine = 0
            count_xarr = [1] * 10
            if count_rarr[arr[row][col]]:
                count_col +=1
                count_rarr[arr[row][col]] =0
            if count_carr[arr[col][row]]:
                count_row +=1
                count_carr[arr[col][row]] =0
            if row % 3 ==0 and col%3 ==0:
                for i in range(3):
                    for j in range(3):
                        rr=row +i
                        cc=col +j
                        if count_xarr[arr[rr][cc]]:
                            count_nine +=1
                            count_xarr[arr[rr][cc]] = 0
                if count_nine ==9:
                    total +=1
        if count_col ==9:
            total += 1
        if count_row ==9:
            total += 1

    if total ==27:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
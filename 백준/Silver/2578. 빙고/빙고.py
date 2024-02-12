board= [list(map(int,input().split())) for _ in range(5)]
chk= [list(map(int,input().split())) for _ in range(5)]
sign = [[1,1,1,1,1] for _ in range(5)]
count_call=0
ans =0
for r in range(5):
    for c in range(5):
        for row in range(5):
            check = count_call
            for col in range(5):
                if chk[r][c] == board[row][col]:
                    sign[row][col]=0
                    count_call +=1
                    if count_call >= 5:
                        chk_bing =0
                        rightup =0
                        leftdown =0
                        for rr in range(5):
                            ro = sum(sign[rr])
                            co = 0
                            for cc in range(5):
                                co += sign[cc][rr]
                                if rr+cc==4:
                                    rightup += sign[rr][cc]
                                if rr==cc:
                                    leftdown += sign[rr][cc]
                            if ro==0:
                                chk_bing +=1
                            if co==0:
                                chk_bing +=1
                        if rightup==0:
                            chk_bing +=1
                        if leftdown==0:
                            chk_bing +=1
                        if chk_bing >=3:
                            ans = count_call
                            print(ans)
                            exit(0)
                        else:
                            break
                    else:
                        break
            if check != count_call:
                break
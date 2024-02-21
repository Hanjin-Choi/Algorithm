def solution(board, moves):
    leng =len(board)
    st=[]
    answer = 0
    for col in moves:
        col -=1
        print(col)
        for row in range(leng):
            if board[row][col]==0:
                continue
            else:
                doll= board[row][col]
                if st and st[-1]==doll:
                    st.pop()
                    answer +=2
                    board[row][col]=0
                else:
                    st.append(doll)
                    board[row][col]=0
                break
    
    print(st)
    
    return answer
c,r = map(int,input().split()) # 가로 세로 입력
arr = [[0]*c for _ in range(r)] # 배열 형성
k= int(input()) # k입력
num=1 # 들어가는 순서
dr=1 # delta index 방향 설정
dc=0
row =col=0
if r*c >=k:#배열에 들어갈수 있으면
    while k>=num: # k번째 까지 돌고 결과 값 반환
        arr[row][col] =num
        if k ==num: # k번째 도달할 경우 아래 수행 X:
            break
        else:
            if 0<=col+dc<c and 0<=row+dr<r and arr[row+dr][col+dc] ==0: # 이동할 위치가 배열 안에 들어 있고 그 숫자가 비어있을때
                row +=dr #이동
                col +=dc
            else:# (1,0)->(0,1)->(-1,0)->(0,-1) 순으로 이동
                if dr: # 이동 방향이 row 방향이었다가 막다른 길에 부딪혔을때
                    dr,dc = dc,dr
                else: # 이동방향이 col 방향이었다가 막다른 길에 부딪혔을때
                    dr,dc = -dc,dr
                row += dr
                col += dc
        num +=1 # 다음 단계로 이동
    print(col+1,row+1) # 0,0시작했으므로 1씩 보정
else:
    print(0)
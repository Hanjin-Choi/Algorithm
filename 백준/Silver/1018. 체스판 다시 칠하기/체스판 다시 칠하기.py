N,M =map(int,input().split())
L = []
for _ in range(N): # 체스판양식 저장
    L.append(list(input()))
c = 0
for i in range(N-7): # 체스판 첫번째 칸 돌기
    for j in range(M-7):
        black = 0
        for a in range(8): # 체스판 8*8호출
            for b in range(8):
                if (a+b) %2 ==0: #임의로 첫칸을 검은색으로 지정시 맞게 칠한 개수 구하기
                    black += (L[a+i][b+j]=="B")
                else:
                    black += (L[a+i][b+j]=="W")    
        if black < 32: #첫칸이 검은색일 경우 틀린 칸이 과반수보다 많은 경우 첫칸을 흰색으로 결정
            black = 64 - black
        if c < black:
            c=black # 맞은 칸의 최대값 비교
print(64-c)
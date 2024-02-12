import sys
input = sys.stdin.readline

n= int(input())
dice = [list(map(int,input().split())) for _ in range(n)]
dice_select = {0: 5, 1: 3, 2: 4, 3: 1, 4: 2, 5: 0} # 주사위 아래면 인덱스 기준으로 윗면의 값을 방출
dp = [0]*7  #첫 다이스의 바닥을 1~6선택했을때 계산을 저장할 리스트
move=[0,1,2,3,4,5,6] # 첫 다이스 기준의 바닥이자, 다음 주사위의 바닥을 저장하기 위한 리스트

for i in range(n): #주사위 호출
    for j in range(1,7): #주사위의 아랫면을 통해 뒤의 연결부위를 확인 + 옆면의 최대값 계산
        temp =dice[i][:]
        lower = move[j] # 아랫면 값을 저장
        lower_index = dice[i].index(lower)
        upper_index = dice_select[lower_index]
        upper = dice[i][upper_index] # 아랫면 기준으로 윗면의 값을 호출
        temp[lower_index]=0 # 아랫면의 값을 temp에서 0으로 반환
        temp[upper_index] =0 # 윗면의 값을 temp에서 0으로 반환
        dp[j] += max(temp) # 옆면의 최대값을 저장
        move[j]=upper # 다음 주사위 검색을 위해 윗면을 아랫면으로 변환

print(max(dp))
res = [['***'], ['* *'], ['***']] # 기본 골자
N = int(input())

while N != 3: # 한번 진행할 때마다 3씩 나누어 3에 도달할 때까지 진행
    l = len(res)
		# 옆으로 3개 붙이기
    for i in range(l):
        res[i] *= 3
		
		# 밑으로 3개 붙이기
    for _ in range(2):
        for i in range(l):
            res.append(res[i].copy())

		# 가운데 부분 공백으로 바꾸기
    for i in range(len(res)):
        if i // l == 1:
            res[i][1] = ' ' * l

		# join으로 묶기
    for i in range(l*3):
        res[i] = [''.join(res[i])]
    
		# 횟수 맞추기
    N //= 3

# 출력
for row in res:
    print(*row)
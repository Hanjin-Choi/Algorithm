N = int(input())
res = [0] * (N+1)
board = [[0] * 1001 for _ in range(1001)]

for num in range(1, N+1):
    x, y, dx, dy = map(int, input().split())

    for i in range(x, x+dx):
        board[i][y:y+dy] = [num] * dy

for r in board:
    for num in range(1, N+1):
        res[num] += r.count(num)

print(*res[1:], sep='\n')
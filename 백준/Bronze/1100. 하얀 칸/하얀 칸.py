arr = [list(input()) for _ in range(8)]
count_mal =0
for row in range(8):
    for col in range(8):
        if (row+col)%2==0 and arr[row][col]=='F':
            count_mal+=1
print(count_mal)
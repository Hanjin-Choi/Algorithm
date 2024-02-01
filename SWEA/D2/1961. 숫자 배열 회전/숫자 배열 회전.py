def spin(array):
    rev_array = list(zip(*array))
    spin_array=[]
    for line in rev_array:
        spin_array.append(line[::-1])
    return spin_array
T= int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    ninety=spin(arr)
    hund_eighty=spin(spin(arr))
    two_hund_seventy=spin(spin(spin(arr)))
    print(f'#{tc}')
    for i in range(N):
        print(*ninety[i],sep='',end=' ')
        print(*hund_eighty[i], sep='', end=' ')
        print(*two_hund_seventy[i], sep='', end='\n')
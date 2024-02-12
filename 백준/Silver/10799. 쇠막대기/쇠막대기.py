arr = list(input())
length = len(arr)
count_cutting =0
stick = 0
for i in range(length):
    if arr[i] == '(':
        if i < length-1 and arr[i+1] == ')':
            count_cutting += stick
        else:
            stick +=1
    elif arr[i] == ')':
        if 1<i and arr[i-1] != '(':
            stick -=1
            count_cutting += 1

print(f'{count_cutting}')
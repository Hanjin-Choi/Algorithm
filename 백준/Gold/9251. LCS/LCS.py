first=input()
second=input()
l1=len(first)+1
l2=len(second)+1
arr= [[0]*l1 for _ in range(l2)]

for row in range(1,l2):
    for col in range(1,l1):
        if first[col-1]==second[row-1]:
            arr[row][col]=arr[row-1][col-1]+1
        else:
            arr[row][col]=max(arr[row-1][col],arr[row][col-1])
print(arr[l2-1][l1-1])
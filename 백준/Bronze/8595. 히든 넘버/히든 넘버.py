n= int(input())
L = input()
suml=0
count_string =1
while count_string <n:
    if L[count_string-1].isnumeric():
        for i in range(count_string,n+1):
            if L[count_string-1:i].isnumeric()==False:
                i-=1
                break
        if i == n:
            suml += int(L[count_string-1:i+1])
        else:
            suml += int(L[count_string-1:i])
        count_string = i
    count_string+=1
print(suml)

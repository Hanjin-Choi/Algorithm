N = int(input())
num = 0
while N:
    if '666' not in str(num):
        num +=1
    else:
        temp = num
        N -=1
        num +=1
print(temp)        

while True:
    s= input()
    if s == '0':
        break
    else:
        ans =1
        for num in s:
            if num =='1':
                ans +=3
            elif num == '0':
                ans +=5
            else:
                ans +=4
        print(ans)
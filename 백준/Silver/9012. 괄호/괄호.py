n=int(input())


for _ in range(n):
    s=input().strip()
    leng = len(s)
    count_bracket = 0
    flag =0
    for i in range(leng):
        if s[i]=='(':
            count_bracket+=1
        else:
            count_bracket -=1
        if count_bracket<0:
            flag=1
            break
    if count_bracket !=0:
        flag=1
    if flag:
        print("NO")
    else:
        print("YES")
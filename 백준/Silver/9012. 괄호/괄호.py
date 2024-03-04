n=int(input())


for _ in range(n):
    s=input().strip()
    leng = len(s)
    st = []
    flag=0
    for i in range(leng):
        if s[i]=='(':
            st.append(s[i])
        elif st and s[i]==')':
            a = st.pop()
            if a!='(':
                flag =1
                break
        else:
            flag =1
            break
    if st:
        flag =1
    if flag:
        print("NO")
    else:
        print("YES")
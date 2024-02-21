def solution(dartResult):
    st =list(dartResult)
    ans=[]
    a=''
    while st:
        s= st.pop(0)
        if s.isdecimal():
            a +=s
            print(a)
        elif s in "SDT":
            a = int(a)
            if s=='S':
                ans.append(a)
            elif s =='D':
                ans.append(a**2)
            elif s =='T':
                ans.append(a**3)
            a= ''
        elif s =='*':
            if len(ans)>1:
                c= ans.pop()
                d = ans.pop()
                ans.append(d*2)
                ans.append(c*2)
                
            else:
                c= ans.pop()
                ans.append(c*2)
        elif s == '#':
            ans[-1] *= -1
            
            
    answer = sum(ans)
    return answer
s=input()
leng=len(s)
st=[]
ans=''
icp={'(':3,'*':2,'/':2,'+':1,'-':1}
isp={'(':0,'*':2,'/':2,'+':1,'-':1}
for i in range(leng):
    if s[i] in '()/*+-':
        if s[i] =='(':
            st.append(s[i])
        elif s[i]==')':
            while st:
                a = st.pop()
                if a!= '(':
                    ans+=a
                else:
                    break
        elif st and isp[st[-1]]>=icp[s[i]]:
            while st and isp[st[-1]]>=icp[s[i]]:
                a= st.pop()
                ans += a
            st.append(s[i])
        else:
            st.append(s[i])
    else:
        ans +=s[i]
while st:
    a= st.pop()
    ans +=a
print(ans)
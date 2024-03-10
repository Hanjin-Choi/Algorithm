s=input()

num =''
st=[]
ans=0
flag=0
for let in s:
    if let.isnumeric():
        num += let
    elif let =='-' and flag==0:
        ans +=int(num)
        num=''
        flag=1
    elif let=='-' and flag==1:
        st.append(int(num))
        num=''
    elif let =='+' and flag==1:
        st.append(int(num))
        num=''
    elif let=='+' and flag==0:
        ans += int(num)
        num=''
if flag==1:
    st.append(int(num))
else:
    ans += int(num)
while st:
    p = st.pop()
    ans -= p
print(ans)

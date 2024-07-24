s=input()
l=input()
st=[]
idx=0
leng=len(l)
for idx in s:
    st.append(idx)
    if ''.join(st[-leng:]) == l:
        for i in range(leng):
            st.pop()
if st:
    print(''.join(st))
else:
    print('FRULA')



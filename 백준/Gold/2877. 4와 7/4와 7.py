n=bin(int(input())+1)
ans=[]
for i in n[3:]:
    if i == '0':
        ans.append('4')
    else:
        ans.append('7')
print(''.join(ans))
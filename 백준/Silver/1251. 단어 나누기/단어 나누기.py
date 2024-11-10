ans =[]
s=input()
leng = len(s)
for i in range(1,leng-1):
    for j in range(i+1,leng):
            new  = s[0:i][::-1] + s[i:j][::-1]+s[j:leng][::-1]
            ans.append(new)
ans.sort()
print(ans[0])
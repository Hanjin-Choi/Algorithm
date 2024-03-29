ans=[0]*26
string =input()
for i in string:
    ans[ord(i)-97] +=1
print(*ans)
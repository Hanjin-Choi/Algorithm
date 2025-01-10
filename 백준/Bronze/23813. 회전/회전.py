n= input()
leng=len(n)
n*=2
ans=0
for i in range(leng):
    ans += int(n[i:i+leng])
print(ans)
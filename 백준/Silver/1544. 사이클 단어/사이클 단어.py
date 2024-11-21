n=int(input())
lst= set()
cnt=0
for _ in range(n):
    s=input()
    leng=len(s)
    if not s in lst:
        cnt+=1
        s*=2
        for i in range(leng):
            lst.add(s[i:i+leng])

print(cnt)

